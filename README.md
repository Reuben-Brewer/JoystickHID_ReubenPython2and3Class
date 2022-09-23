###########################

JoystickHID_ReubenPython2and3Class

Wrapper of pygame (including ability to hook to Tkinter GUI and some useful button-latching functionality) for reading USB HID (Human Interface Device) joysticks (like VKBsim Gladiator).

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com

www.reubotics.com

Apache 2 License

Software Revision F, 09/21/2022

Verified working on: 

Python 2.7, 3.8.

Windows 8.1, 10 64-bit

Ubuntu 20.04*

Raspberry Pi Buster 

(no Mac testing yet)

*Note: This code mostly works in Ubuntu 20.04, but the hat yields strange values for some models of joystick (such as the VKBsim Gladiator).

Running jstest-gtk (sudo apt-get install jstest-gtk) will show you what the actual values are that are streaming from the joystick without going through JoystickHID_ReubenPython2and3Class.*

###########################

########################### Python module installation instructions, all OS's

JoystickHID_ReubenPython2and3Class, ListOfModuleDependencies: ['future.builtins', 'Joystick2DdotDisplay_ReubenPython2and3Class', 'pygame']

JoystickHID_ReubenPython2and3Class, ListOfModuleDependencies_TestProgram: ['MyPrint_ReubenPython2and3Class']

JoystickHID_ReubenPython2and3Class, ListOfModuleDependencies_NestedLayers: ['future.builtins']

JoystickHID_ReubenPython2and3Class, ListOfModuleDependencies_All: ['future.builtins', 'Joystick2DdotDisplay_ReubenPython2and3Class', 'MyPrint_ReubenPython2and3Class', 'pygame']

#https://github.com/Reuben-Brewer/Joystick2DdotDisplay_ReubenPython2and3Class

from Joystick2DdotDisplay_ReubenPython2and3Class import *

#"pip install pygame" or "pip install pygame_VersionInfo.whl"

import pygame

###########################
