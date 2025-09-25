import pywinusb.hid as hid
from pynput import keyboard
import time
import threading

# VID:PID for Ranked Guardian G65 (get from device manager or better usbdeview tool)
VID = 0x3532
PID = 0xA0C1

# Profile 1 usb payload for rgb preset "lighting by press" (preset 3)  speed 4 brightness 2  (figured these out with wireshark and usbpcap )
profile1_64 = bytearray.fromhex("04ae0100000304020100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")

# Profile 2 usb payload for rgb preset "Stars" (preset 4) speed 0 brightness 1 
profile2_64 = bytearray.fromhex("04ae0100000400010100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")

idle_timeout = 5  # 10 seconds idle timeout

last_activity = time.time()

current_profile = profile1_64

# Example profile for Custom RGB preset
# Profile 3 payload for a CUSTOM rgb preset with all keys set to a nice pastel green brightness 1
# profile3_64 = bytearray.fromhex("04ae010000140501ff9571ff499671ff499771ff499871ff499971ff499a71ff499b71ff499c71ff499d71ff499e71ff499f71ff49a071ff49a171ff49000000")

def send_profile(profile):
    filter = hid.HidDeviceFilter(vendor_id=VID, product_id=PID)
    devices = filter.get_devices()
    device = devices[0]
    device.open()
    device.send_output_report(profile)
    device.close()

def on_press(key):
    global last_activity
    global current_profile
    if current_profile != profile1_64:
        send_profile(profile1_64)
        current_profile = profile1_64
        last_activity = time.time()
    else:
        last_activity = time.time()

listener = keyboard.Listener(on_press=on_press)
listener.start()


def main():
    global last_activity
    global current_profile        


    if time.time() - last_activity > idle_timeout:
        print("idle")
        if current_profile == profile2_64:
            time.sleep(idle_timeout)
            return main()
        else:
            last_activity = time.time()

            filter = hid.HidDeviceFilter(vendor_id=VID, product_id=PID)
            devices = filter.get_devices()
            if not devices:
                time.sleep(idle_timeout)
                return main()
            else:
                send_profile(profile2_64)
                current_profile = profile2_64
                last_activity = time.time()
                time.sleep(idle_timeout)
                return main()
    else:
        time.sleep(idle_timeout)
        return main()

if __name__ == "__main__":
    main()