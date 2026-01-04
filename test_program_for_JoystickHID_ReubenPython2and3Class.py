# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision K, 12/27/2025

Verified working on: Python 3.11/12/13 for Windows 10/11 64-bit, Ubuntu 20.04*, and Raspberry Pi Bookworm.

*Note: This code mostly works in Ubuntu 20.04, but the hat yields strange values for some models of Joystick
(such as the VKBsim Gladiator). Running jstest-gtk (sudo apt-get install jstest-gtk) will show you what the
actual values are that are streaming from the Joystick without going through JoystickHID_ReubenPython2and3Class.*
'''

__author__ = 'reuben.brewer'

##########################################################################################################
##########################################################################################################

#########################################################
import ReubenGithubCodeModulePaths #Replaces the need to have "ReubenGithubCodeModulePaths.pth" within "C:\Anaconda3\Lib\site-packages".
ReubenGithubCodeModulePaths.Enable()
#########################################################

#########################################################
from JoystickHID_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *
#########################################################

#########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
import argparse
import keyboard
#########################################################

#########################################################
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
#########################################################

#########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#########################################################

##########################################################################################################
##########################################################################################################

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global JoystickHID_Object
    global JoystickHID_OPEN_FLAG
    global SHOW_IN_GUI_Joystick_FLAG

    global MyPrint_Object
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if JoystickHID_OPEN_FLAG == 1 and SHOW_IN_GUI_Joystick_FLAG == 1:
                JoystickHID_Object.GUI_update_clock()
            #########################################################

            #########################################################
            if MyPrint_OPEN_FLAG == 1 and SHOW_IN_GUI_MyPrint_FLAG == 1:
                MyPrint_Object.GUI_update_clock()
            #########################################################

            #########################################################
            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
            #########################################################

        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback(OptionalArugment = 0):
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    global JoystickHID_Object
    global JoystickHID_OPEN_FLAG

    global MyPrint_Object
    global MyPrint_OPEN_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()

    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_JoystickHID_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_Joystick
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_Joystick = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_Joystick, text='   Joystick   ')

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        TabControlObject.grid(row=0, column=0, sticky='nsew')

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############

        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_Joystick = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    #################################################
    #################################################
    if JoystickHID_OPEN_FLAG == 1:
        JoystickHID_Object.CreateGUIobjects(TkinterParent=Tab_Joystick)
    #################################################
    #################################################

    #################################################
    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_Object.CreateGUIobjects(TkinterParent=Tab_MyPrint)
    #################################################
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    #################################################
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    #################################################
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    #################################################
    #################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    Joystick_NameDesired = "" #"" means that we don't care about the name.
    #Joystick_NameDesired = "VKBsim Gladiator"
    #Joystick_NameDesired = "3Dconnexion KMJ Emulator"
    #Joystick_NameDesired = "vJoy Device"
    #Joystick_NameDesired = "Tetherscript Virtual Joystick" #Position-control input on all axes
    #Joystick_NameDesired = "SpaceMouse Compact" #Rate-control input on all axes (integrates values when off-center)
    #Joystick_NameDesired = "Core (Plus) Wired Controller" #NintendoSwitch wired controller by Core, doesn't support rumble.
    #Joystick_NameDesired = "PS4 Controller" #DualShock4 for PS4. Rumble works when the controller is plugged-in but not in wireless/bluetooth mode. Didn't need any special drivers for Windows.
    #Joystick_NameDesired = "DualSense Wireless Controller" #DualSense for PS5. Doesn't work if both the DualSense for PS5 and DualShock for PS4 are both connected via Bluetooth simultaneously. Rumble works when the controller is plugged-in but not in wireless/bluetooth mode.
    #Joystick_NameDesired = "Nintendo Switch Pro Controller"
    #Joystick_NameDesired = DOES NOT WORK: "Controller (Xbox One For Windows)" #Name when plugged-in via USB-C. Rumble works both in wireless/wired modes. Only trigger axes work.
    #Joystick_NameDesired = DOES NOT WORK: "Xbox Series X Controller" #Name when connected via Bluetooth

    #Joystick_NameDesired = "UHID Gamepad Device #1"

    Joystick_IntegerIDdesired = -1 #means that we don't care about the IntegerID.
    Joystick_ShowJustDotMovingFlag = 0
    Joystick_Axis_Index_ToDisplayAsHorizontalAxisOn2DdotDisplay = 0
    Joystick_Axis_Index_ToDisplayAsVerticalAxisOn2DdotDisplay = 1
    Joystick_Button_IndexList_ToDisplayAsDotColorOn2DdotDisplay = [9, 10, 13]
    Joystick_PrintInfoForAllDetectedJoysticksFlag = 1
    Joystick_SearchAllJoysticksFlag = 1 #IMPORTANT: if opening by the joystick's name ONLY, then you must set "SearchAllJoysticksFlag" to 1.

    #For instance, the name "UHID Gamepad Device #4" would yield Joystick_IntegerIDdetected_ExtractedFromJoystickName = 4.
    #Pygame would still open by Joystick_IntegerIDdetected, but we would match-and-open the detected joystick by Joystick_IntegerIDdetected_ExtractedFromJoystickName.
    Joystick_AllowNumberSymbolInJoystickNameDetectedToOverrideJoystickIntegerIDdetectedFlag = 0
    #################################################
    #################################################

    ################################################# Put the argv parsing AFTER the parameter hard-coding so that we can over-ride it if desired.
    #################################################
    argparse_Object = argparse.ArgumentParser()
    #nargs='?', const='arg_was_not_given' is the key to allowing us to not input an argument (use Pycharm "run")
    argparse_Object.add_argument("-i", "--IntegerIDdesired", nargs='?', const='arg_was_not_given', required=False, help="IntegerIDdesired (integer)")
    argparse_Object.add_argument("-n", "--NameDesired", nargs='?', const='arg_was_not_given', required=False, help="NameDesired (string)")
    argparse_Object.add_argument("-s", "--SearchAllJoysticksFlag", nargs='?', const='arg_was_not_given', required=False, help="SearchAllJoysticksFlag (0/1)")
    argparse_Object.add_argument("-a", "--AllowNumberSymbolInJoystickNameDetectedToOverrideJoystickIntegerIDdetectedFlag", nargs='?', const='arg_was_not_given', required=False, help="AllowNumberSymbolInJoystickNameDetectedToOverrideJoystickIntegerIDdetectedFlag (0/1)")
    ARGV_Dict = vars(argparse_Object.parse_args())
    print("ARGV_Dict: " + str(ARGV_Dict))

    ################################################# PUTTING THIS AFTER EVERYTHING SO THAT WE CAN OVERRIDE -P FILE OPTIONS
    if ARGV_Dict["IntegerIDdesired"] != None and ARGV_Dict["NameDesired"] == None:
        Joystick_IntegerIDdesired = int(ARGV_Dict["IntegerIDdesired"])
        Joystick_NameDesired = "" #Let any english string name be used.

    print("Joystick_IntegerIDdesired: " + str(Joystick_IntegerIDdesired))
    #################################################

    #################################################
    if ARGV_Dict["NameDesired"] != None and ARGV_Dict["IntegerIDdesired"] == None:
        Joystick_NameDesired = str(ARGV_Dict["NameDesired"])
        Joystick_IntegerIDdesired = -1 #Let any integer ID be used.

    print("Joystick_NameDesired: " + str(Joystick_NameDesired))
    #################################################

    #################################################
    if ARGV_Dict["NameDesired"] != None and ARGV_Dict["IntegerIDdesired"] != None:
        Joystick_IntegerIDdesired = int(ARGV_Dict["IntegerIDdesired"])
        Joystick_NameDesired = str(ARGV_Dict["NameDesired"])

    print("Joystick_IntegerIDdesired: " + str(Joystick_IntegerIDdesired))
    print("Joystick_NameDesired: " + str(Joystick_NameDesired))
    #################################################

    #################################################
    if ARGV_Dict["SearchAllJoysticksFlag"] != None:
        Joystick_SearchAllJoysticksFlag = str(ARGV_Dict["SearchAllJoysticksFlag"])

    print("Joystick_SearchAllJoysticksFlag: " + str(Joystick_SearchAllJoysticksFlag))
    #################################################

    #################################################
    if ARGV_Dict["AllowNumberSymbolInJoystickNameDetectedToOverrideJoystickIntegerIDdetectedFlag"] != None:
        Joystick_AllowNumberSymbolInJoystickNameDetectedToOverrideJoystickIntegerIDdetectedFlag = str(ARGV_Dict["AllowNumberSymbolInJoystickNameDetectedToOverrideJoystickIntegerIDdetectedFlag"])

    print("Joystick_AllowNumberSymbolInJoystickNameDetectedToOverrideJoystickIntegerIDdetectedFlag: " + str(Joystick_AllowNumberSymbolInJoystickNameDetectedToOverrideJoystickIntegerIDdetectedFlag))
    #################################################

    #################################################
    #################################################

    #################################################
    #################################################
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1

    global USE_Joystick_FLAG
    USE_Joystick_FLAG = 1

    global USE_MyPrint_FLAG
    USE_MyPrint_FLAG = 1

    global USE_KEYBOARD_FLAG
    USE_KEYBOARD_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_Joystick_FLAG
    SHOW_IN_GUI_Joystick_FLAG = 1

    global SHOW_IN_GUI_MyPrint_FLAG
    SHOW_IN_GUI_MyPrint_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_Joystick
    global GUI_COLUMN_Joystick
    global GUI_PADX_Joystick
    global GUI_PADY_Joystick
    global GUI_ROWSPAN_Joystick
    global GUI_COLUMNSPAN_Joystick
    GUI_ROW_Joystick = 1

    GUI_COLUMN_Joystick = 0
    GUI_PADX_Joystick = 1
    GUI_PADY_Joystick = 1
    GUI_ROWSPAN_Joystick = 1
    GUI_COLUMNSPAN_Joystick = 1

    global GUI_ROW_MyPrint
    global GUI_COLUMN_MyPrint
    global GUI_PADX_MyPrint
    global GUI_PADY_MyPrint
    global GUI_ROWSPAN_MyPrint
    global GUI_COLUMNSPAN_MyPrint
    GUI_ROW_MyPrint = 2

    GUI_COLUMN_MyPrint = 0
    GUI_PADX_MyPrint = 1
    GUI_PADY_MyPrint = 1
    GUI_ROWSPAN_MyPrint = 1
    GUI_COLUMNSPAN_MyPrint = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global ResetLatchedValuesTime
    ResetLatchedValuesTime = -11111.0

    global root

    global root_Xpos
    root_Xpos = 900

    global root_Ypos
    root_Ypos = 0

    global root_width
    root_width = 1920 - root_Xpos

    global root_height
    root_height = 1020 - root_Ypos

    global TabControlObject
    global Tab_MainControls
    global Tab_Joystick
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30
    #################################################
    #################################################

    #################################################
    #################################################
    global JoystickHID_Object

    global JoystickHID_OPEN_FLAG
    JoystickHID_OPEN_FLAG = -1

    global Joystick_MostRecentDict
    Joystick_MostRecentDict = dict()

    global Joystick_MostRecentDict_Joystick_Axis_Value_List
    Joystick_MostRecentDict_Joystick_Axis_Value_List = list()

    global Joystick_MostRecentDict_Joystick_Button_Value_List
    Joystick_MostRecentDict_Joystick_Button_Value_List = list()

    global Joystick_MostRecentDict_Joystick_Button_LatchingRisingEdgeEvents_List
    Joystick_MostRecentDict_Joystick_Button_LatchingRisingEdgeEvents_List = list()

    global Joystick_MostRecentDict_Joystick_Hat_Value_List
    Joystick_MostRecentDict_Joystick_Hat_Value_List = list()

    global Joystick_MostRecentDict_Joystick_Hat_LatchingRisingEdgeEvents_List
    Joystick_MostRecentDict_Joystick_Hat_LatchingRisingEdgeEvents_List = list()

    global Joystick_MostRecentDict_Joystick_Ball_Value_List
    Joystick_MostRecentDict_Joystick_Ball_Value_List = list()

    global Joystick_MostRecentDict_DataStreamingFrequency
    Joystick_MostRecentDict_DataStreamingFrequency = -11111.0

    global Joystick_MostRecentDict_Time
    Joystick_MostRecentDict_Time = -11111.0
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_Object

    global MyPrint_OPEN_FLAG
    MyPrint_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_KEYBOARD_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        keyboard.on_press_key("esc", ExitProgram_Callback)
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global JoystickHID_GUIparametersDict
    JoystickHID_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_Joystick_FLAG),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_Joystick),
                                    ("GUI_COLUMN", GUI_COLUMN_Joystick),
                                    ("GUI_PADX", GUI_PADX_Joystick),
                                    ("GUI_PADY", GUI_PADY_Joystick),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_Joystick),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_Joystick)])

    global JoystickHID_SetupDict
    JoystickHID_SetupDict = dict([("GUIparametersDict", JoystickHID_GUIparametersDict),
                                                                ("NameToDisplay_UserSet", "Reuben's JoystickHID_ReubenPython2and3Class Test"),
                                                                ("Joystick_NameDesired", Joystick_NameDesired),
                                                                ("Joystick_IntegerIDdesired", Joystick_IntegerIDdesired),
                                                                ("Joystick_ShowJustDotMovingFlag", Joystick_ShowJustDotMovingFlag),
                                                                ("Joystick_Axis_Index_ToDisplayAsHorizontalAxisOn2DdotDisplay", Joystick_Axis_Index_ToDisplayAsHorizontalAxisOn2DdotDisplay),
                                                                ("Joystick_Axis_Index_ToDisplayAsVerticalAxisOn2DdotDisplay", Joystick_Axis_Index_ToDisplayAsVerticalAxisOn2DdotDisplay),
                                                                ("Joystick_Button_IndexList_ToDisplayAsDotColorOn2DdotDisplay", Joystick_Button_IndexList_ToDisplayAsDotColorOn2DdotDisplay),
                                                                ("MainThread_TimeToSleepEachLoop", 0.010),
                                                                ("Joystick_PrintInfoForAllDetectedJoysticksFlag", Joystick_PrintInfoForAllDetectedJoysticksFlag),
                                                                ("Joystick_SearchAllJoysticksFlag", Joystick_SearchAllJoysticksFlag),
                                                                ("AllowNumberSymbolInJoystickNameDetectedToOverrideJoystickIntegerIDdetectedFlag", Joystick_AllowNumberSymbolInJoystickNameDetectedToOverrideJoystickIntegerIDdetectedFlag)])

    if USE_Joystick_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        try:
            JoystickHID_Object = JoystickHID_ReubenPython2and3Class(JoystickHID_SetupDict)
            JoystickHID_OPEN_FLAG = JoystickHID_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("JoystickHID_Object __init__: Exceptions: %s" % exceptions)
            #traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_Joystick_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if JoystickHID_OPEN_FLAG != 1:
                print("Failed to open JoystickHID_ReubenPython2and3Class.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    #################################################
    #################################################
    global MyPrint_Object_GUIparametersDict
    MyPrint_Object_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MyPrint_FLAG),
                                            ("UseBorderAroundThisGuiObjectFlag", 0),
                                            ("GUI_ROW", GUI_ROW_MyPrint),
                                            ("GUI_COLUMN", GUI_COLUMN_MyPrint),
                                            ("GUI_PADX", GUI_PADX_MyPrint),
                                            ("GUI_PADY", GUI_PADY_MyPrint),
                                            ("GUI_ROWSPAN", GUI_ROWSPAN_MyPrint),
                                            ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MyPrint)])

    global MyPrint_Object_SetupDict
    MyPrint_Object_SetupDict = dict([("NumberOfPrintLines", 10),
                                    ("WidthOfPrintingLabel", 200),
                                    ("PrintToConsoleFlag", 1),
                                    ("LogFileNameFullPath", os.path.join(os.getcwd(), "TestLog.txt")),
                                    ("GUIparametersDict", MyPrint_Object_GUIparametersDict)])

    if USE_MyPrint_FLAG == 1:
        try:
            MyPrint_Object = MyPrint_ReubenPython2and3Class(MyPrint_Object_SetupDict)
            MyPrint_OPEN_FLAG = MyPrint_Object.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_Object __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
            if MyPrint_OPEN_FLAG != 1:
                print("Failed to open MyPrint_Object.")
                ExitProgram_Callback()
    #################################################
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## KEY GUI LINE
    ##########################################################################################################
    ##########################################################################################################
    if USE_GUI_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread, daemon=True) #Daemon=True means that the GUI thread is destroyed automatically when the main thread is destroyed
        GUI_Thread_ThreadingObject.start()
    else:
        root = None
        Tab_MainControls = None
        Tab_Joystick = None
        Tab_MyPrint = None
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    print("Starting main loop 'test_program_for_JoystickHID_ReubenPython2and3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        ###################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################
        ###################################################

        ################################################### GET's
        ###################################################
        if JoystickHID_OPEN_FLAG == 1:

            Joystick_MostRecentDict = JoystickHID_Object.GetMostRecentDataDict()

            if "Time" in Joystick_MostRecentDict:
                Joystick_MostRecentDict_Joystick_Axis_Value_List = Joystick_MostRecentDict["Joystick_Axis_Value_List"]
                Joystick_MostRecentDict_Joystick_Button_Value_List = Joystick_MostRecentDict["Joystick_Button_Value_List"]
                Joystick_MostRecentDict_Joystick_Button_LatchingRisingEdgeEvents_List = Joystick_MostRecentDict["Joystick_Button_LatchingRisingEdgeEvents_List"]
                Joystick_MostRecentDict_Joystick_Hat_Value_List = Joystick_MostRecentDict["Joystick_Hat_Value_List"]
                Joystick_MostRecentDict_Joystick_Hat_LatchingRisingEdgeEvents_List = Joystick_MostRecentDict["Joystick_Hat_LatchingRisingEdgeEvents_List"]
                Joystick_MostRecentDict_Joystick_Ball_Value_List = Joystick_MostRecentDict["Joystick_Ball_Value_List"]
                Joystick_MostRecentDict_DataStreamingFrequency = Joystick_MostRecentDict["DataStreamingFrequency"]
                Joystick_MostRecentDict_Time = Joystick_MostRecentDict["Time"]

                #print("Joystick_MostRecentDict: " + str(Joystick_MostRecentDict))
                #print("Joystick_MostRecentDict_Joystick_Axis_Value_List: " + str(Joystick_MostRecentDict_Joystick_Axis_Value_List))
        ###################################################
        ###################################################

        ################################################### SET's
        ###################################################
        if JoystickHID_OPEN_FLAG == 1 and (CurrentTime_MainLoopThread - ResetLatchedValuesTime >= 5.0):
            #JoystickHID_Object.ResetButtonRisingEdgeEventLatch(13)
            #JoystickHID_Object.ResetButtonRisingEdgeEventLatch(17)
            #JoystickHID_Object.ResetHatRisingEdgeEventLatch(0, 0)
            #JoystickHID_Object.ResetHatRisingEdgeEventLatch(0, 1)

            JoystickHID_Object.Rumble(Rumble_LowFrequencyMotor_Strength0to1=1.0, Rumble_HighFrequencyMotor_Strength0to1=1.0, Rumble_DurationMilliseconds=1000)

            ResetLatchedValuesTime = CurrentTime_MainLoopThread
        ###################################################
        ###################################################

        time.sleep(0.002)
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## THIS IS THE EXIT ROUTINE!
    ##########################################################################################################
    ##########################################################################################################
    print("Exiting main program 'test_program_for_JoystickHID_ReubenPython2and3Class.")

    #################################################
    if JoystickHID_OPEN_FLAG == 1:
        JoystickHID_Object.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_Object.ExitProgram_Callback()
    #################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################