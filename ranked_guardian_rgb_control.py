import pywinusb.hid as hid
from pynput import keyboard
import time
import threading

# VID:PID for Ranked Guardian G65 (get from device manager or better usbdeview tool)
VID = 0x3532
PID = 0xA0C1

# Profile 1 payload for rgb preset "lighting by press" (preset 3)  speed 4 brightness 2  (figured these out with wireshark and usbpcap )
profile1_64 = bytearray.fromhex("04ae0100000304020100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")

# Profile 2 payload for rgb preset "Stars" (preset 4) speed 0 brightness 1 
profile2_64 = bytearray.fromhex("04ae0100000400010100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")

# Example profile for Custom RGB preset
# Profile 3 payload for a CUSTOM rgb preset with all keys set to a nice pastel green brightness 1  (figured these out with wireshark and usbpcap )
# profile3_64 = bytearray.fromhex("04ae010000140501ff9571ff499671ff499771ff499871ff499971ff499a71ff499b71ff499c71ff499d71ff499e71ff499f71ff49a071ff49a171ff49000000")


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