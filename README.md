# ranked_guardian_G65_rgb_control
Get programable controll over your rgb profiles on a Ranked Guardian G65 Keyboard

Automatically switches to Profile 1 on keypress.
Reverts to Profile 2 after 10 seconds of no keyboard activity.
Runs silently in the background using pythonw.exe.
Configurable to start automatically on Windows startup.

## This is an example script! 

You now have full programmable control over the rgb profiles and if think this further modify this script to your needs like for example:

- turning on backgroundlighting only in the evening

- switch profile when new email arrived

- switch custom profiles per foreground app

- switch custom profiles when holding altgr fn or fn2

- or combine all these or whatever floats your boat. With python you have deepest integration and almost every signal in the pc at your disposle:)


## Prerequisites

- Windows operating system.

- Python 3.10 ( 3.6 or higher but only tested with 3.10 ).

- Ranked Guardian G65 keyboard (VID: 0x3532, PID: 0xA0C1) connected.

# Installation

- Download the Script

- Install required Python libraries:

- pip install pywinusb pynput

# Running on Windows Startup

- Locate pythonw.exe in your Python installation (e.g., C:\Python39\pythonw.exe).

- Right-click ranked_guardian_rgb_control.py, select "Create shortcut.

- Right-click the shortcut, select "Properties," and set:

- Target: "C:\Python39\pythonw.exe" "C:\Users\<YourUsername>\Desktop\keyboard-rgb-control\keyboard_rgb_control.py"

- Start in: C:\Users\<YourUsername>\Desktop\keyboard-rgb-controlReplace paths with your actual Python and script locations.

- Move the shortcut to the Startup folder.

The script will now run hidden automatically when you log into Windows.


# Retrieving the color profiles

the script contains  two example profiles as hex code. 

if you want to use other profiles you have to grab them yourself !

short Tutorial: 

install ranked utility from ranked website (you should have this installed already)

install wireshark with usbpcap driver 

run C:\Program Files\USBPcap\USBPcapCMD.exe to record the usb throughput 

set your profiles in ranked utility 

then close USBPcapCMD.exe

and drag the recorded file into wireshark 

in wireshark you will see such a sequence for every rgb profile change 

<img width="663" height="71" alt="image" src="https://github.com/user-attachments/assets/76151e9a-0175-4fc2-a17a-33c8b8d85dd5" />

only the first entry is important !!! double click and scroll down to hid data 

rightclick hid data and copy as hexstream and use in your script :)

# this also enables you to use as many custom rgb profiles as you want, while originally the keyboard software only supports one custom rgb profile!!!
just create a custom profile send it to the keyboard and capture it with usbpcapCMD.exe


License
MIT License - feel free to modify and distribute.
