###########################

JoystickHID_ReubenPython2and3Class

Wrapper of pygame (including ability to hook to Tkinter GUI and some useful button-latching functionality) for reading USB HID (Human Interface Device) joysticks (like VKBsim Gladiator).

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com

www.reubotics.com

Apache 2 License

Software Revision J, 06/23/2025

Verified working on:

Python 3.11/12.

Windows 10/11 64-bit

Ubuntu 20.04*

Raspberry Pi Bookworm

*Note: This code mostly works in Ubuntu 20.04, but the hat yields strange values for some models of joystick (such as the VKBsim Gladiator).
Running jstest-gtk (sudo apt-get install jstest-gtk) will show you what the actual values are that are streaming from the joystick without going through JoystickHID_ReubenPython2and3Class.*

**Note: If opening more than one joystick at a time, sometimes the order in which the joysticks are opened matters.
For instance, in Windows 10, if we're opening both a "VKBsim Gladiator" and "Nintendo Switch Pro Controller",
the "Nintendo Switch Pro Controller" must be opened first (or else it will stop streaming data once the "VKBsim Gladiator" is opened).

***Note: IMPORTANT: if opening by the joystick's name ONLY (with integer ID = -1), then you must set "SearchAllJoysticksFlag" to 1.

Have tested on the following joysticks:

*Joystick_NameDesired = "VKBsim Gladiator"

*Joystick_NameDesired = "3Dconnexion KMJ Emulator"

*Joystick_NameDesired = "vJoy Device"

*Joystick_NameDesired = "Tetherscript Virtual Joystick"

*Joystick_NameDesired = "SpaceMouse Compact"

*Joystick_NameDesired = "Core (Plus) Wired Controller" #NintendoSwitch wired controller by Core, doesn't support rumble.

*Joystick_NameDesired = "PS4 Controller" #DualShock4 for PS4. Rumble works when the controller is plugged-in but not in wireless/bluetooth mode. Didn't need any special drivers for Windows.

*Joystick_NameDesired = "DualSense Wireless Controller" #DualSense for PS5. Doesn't work if both the DualSense for PS5 and DualShock for PS4 are both connected via Bluetooth simultaneously. Rumble works when the controller is plugged-in but not in wireless/bluetooth mode.

*Joystick_NameDesired = "Nintendo Switch Pro Controller"

*Joystick_NameDesired = DOES NOT WORK: "Controller (Xbox One For Windows)" #Name when plugged-in via USB-C. Rumble works both in wireless/wired modes. Only trigger axes work.

*Joystick_NameDesired = DOES NOT WORK: "Xbox Series X Controller" #Name when connected via Bluetooth

###########################

########################### Python module installation instructions, all OS's

JoystickHID_ReubenPython2and3Class, ListOfModuleDependencies: ['future.builtins', 'Joystick2DdotDisplay_ReubenPython2and3Class', 'pygame']

JoystickHID_ReubenPython2and3Class, ListOfModuleDependencies_TestProgram: ['MyPrint_ReubenPython2and3Class']

JoystickHID_ReubenPython2and3Class, ListOfModuleDependencies_NestedLayers: ['future.builtins']

JoystickHID_ReubenPython2and3Class, ListOfModuleDependencies_All:['future.builtins', 'Joystick2DdotDisplay_ReubenPython2and3Class', 'MyPrint_ReubenPython2and3Class', 'pygame']

#https://github.com/Reuben-Brewer/Joystick2DdotDisplay_ReubenPython2and3Class

from Joystick2DdotDisplay_ReubenPython2and3Class import *

#"pip install pygame" or "pip install pygame_VersionInfo.whl"

import pygame

###########################