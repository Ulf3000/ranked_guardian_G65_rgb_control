import pywinusb.hid as hid
from pynput import keyboard
import time
import threading

# VID:PID for Ranked Guardian G65 (get from device manager or better usbdeview tool)
VID = 0x3532
PID = 0xA0C1

# Profile 1 payload for rgb preset "lighting by press"   (figured these out with wireshark and usbpcap )
profile1_64 = bytearray.fromhex(
    '04 ae 01 00 00 03 07 04 00 00 00 00 00 00 00 00 '
    '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 '
    '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 '
    '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
)

# Profile 2 payload for rgb preset "Stars"
profile2_64 = bytearray.fromhex(
    '04 ae 01 00 00 04 05 04 01 00 00 00 00 00 00 00 '
    '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 '
    '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 '
    '00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'
)

def find_and_open_device():
    filter = hid.HidDeviceFilter(vendor_id=VID, product_id=PID)
    devices = filter.get_devices()
    if not devices:
        raise ValueError("Keyboard not found. Check VID:PID or plug in.")
    device = devices[0]
    device.open()
    return device

def send_profile(device, profile):
    try:
        device.send_output_report(profile)
        profile_name = "Profile 1" if profile == profile1_64 else "Profile 2"
        print(f"{profile_name} sent!")
    except Exception as e:
        print(f"Error sending profile: {e}")

def main():
    try:
        device = find_and_open_device()
        last_activity = time.time()
        current_profile = profile2_64  # Start with profile2
        send_profile(device, current_profile)
        idle_timeout = 10  # 10 seconds idle timeout

        def on_press(key):
            nonlocal last_activity, current_profile
            last_activity = time.time()
            if current_profile != profile1_64:
                current_profile = profile1_64
                send_profile(device, profile1_64)

        def check_idle():
            nonlocal last_activity, current_profile
            while True:
                if time.time() - last_activity > idle_timeout and current_profile != profile2_64:
                    current_profile = profile2_64
                    send_profile(device, profile2_64)
                time.sleep(1)

        # Start idle checker in a separate thread
        idle_thread = threading.Thread(target=check_idle, daemon=True)
        idle_thread.start()

        # Start non-blocking keyboard listener
        listener = keyboard.Listener(on_press=on_press)
        listener.start()

        # Keep the script running
        while True:
            time.sleep(1)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            device.close()
        except:
            pass

if __name__ == "__main__":
    main()