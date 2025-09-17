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

- switch depending on foreground app 

- whatever floats your boat with python you have deepest integration :)


## Prerequisites

- Windows operating system.

- Python 3.6 or higher.

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


License
MIT License - feel free to modify and distribute.
