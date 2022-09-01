# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision E, 08/29/2022

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

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
#########################################################

#########################################################
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
#########################################################

#########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#########################################################

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def TestButtonResponse():
    global MyPrint_ReubenPython2and3ClassObject
    global USE_MYPRINT_FLAG

    if USE_MYPRINT_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.my_print("Test Button was Pressed!")
    else:
        print("Test Button was Pressed!")
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global JoystickHID_ReubenPython2and3ClassObject
    global JOYSTICK_OPEN_FLAG
    global SHOW_IN_GUI_JOYSTICK_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MYPRINT_OPEN_FLAG
    global SHOW_IN_GUI_MYPRINT_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if JOYSTICK_OPEN_FLAG == 1 and SHOW_IN_GUI_JOYSTICK_FLAG == 1:
                JoystickHID_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if MYPRINT_OPEN_FLAG == 1 and SHOW_IN_GUI_MYPRINT_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback():
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

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_JOYSTICK
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_JOYSTICK = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_JOYSTICK, text='   JOYSTICK   ')

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############
        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_JOYSTICK = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    #################################################
    TestButton = Button(Tab_MainControls, text='Test Button', state="normal", width=20, command=lambda i=1: TestButtonResponse())
    TestButton.grid(row=0, column=0, padx=5, pady=1)
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_JoystickHID_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################

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
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1

    global USE_JOYSTICK_FLAG
    USE_JOYSTICK_FLAG = 1

    global USE_MYPRINT_FLAG
    USE_MYPRINT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_JOYSTICK_FLAG
    SHOW_IN_GUI_JOYSTICK_FLAG = 1

    global SHOW_IN_GUI_MYPRINT_FLAG
    SHOW_IN_GUI_MYPRINT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_JOYSTICK
    global GUI_COLUMN_JOYSTICK
    global GUI_PADX_JOYSTICK
    global GUI_PADY_JOYSTICK
    global GUI_ROWSPAN_JOYSTICK
    global GUI_COLUMNSPAN_JOYSTICK
    GUI_ROW_JOYSTICK = 1

    GUI_COLUMN_JOYSTICK = 0
    GUI_PADX_JOYSTICK = 1
    GUI_PADY_JOYSTICK = 1
    GUI_ROWSPAN_JOYSTICK = 1
    GUI_COLUMNSPAN_JOYSTICK = 1

    global GUI_ROW_MYPRINT
    global GUI_COLUMN_MYPRINT
    global GUI_PADX_MYPRINT
    global GUI_PADY_MYPRINT
    global GUI_ROWSPAN_MYPRINT
    global GUI_COLUMNSPAN_MYPRINT
    GUI_ROW_MYPRINT = 2

    GUI_COLUMN_MYPRINT = 0
    GUI_PADX_MYPRINT = 1
    GUI_PADY_MYPRINT = 1
    GUI_ROWSPAN_MYPRINT = 1
    GUI_COLUMNSPAN_MYPRINT = 1
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
    global Tab_JOYSTICK
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30
    #################################################
    #################################################

    #################################################
    #################################################
    global JoystickHID_ReubenPython2and3ClassObject

    global JOYSTICK_OPEN_FLAG
    JOYSTICK_OPEN_FLAG = -1

    global JOYSTICK_MostRecentDict
    JOYSTICK_MostRecentDict = dict()

    global JOYSTICK_MostRecentDict_Joystick_Axis_Value_List
    JOYSTICK_MostRecentDict_Joystick_Axis_Value_List = list()

    global JOYSTICK_MostRecentDict_Joystick_Button_Value_List
    JOYSTICK_MostRecentDict_Joystick_Button_Value_List = list()

    global JOYSTICK_MostRecentDict_Joystick_Button_LatchingRisingEdgeEvents_List
    JOYSTICK_MostRecentDict_Joystick_Button_LatchingRisingEdgeEvents_List = list()

    global JOYSTICK_MostRecentDict_Joystick_Hat_Value_List
    JOYSTICK_MostRecentDict_Joystick_Hat_Value_List = list()

    global JOYSTICK_MostRecentDict_Joystick_Hat_LatchingRisingEdgeEvents_List
    JOYSTICK_MostRecentDict_Joystick_Hat_LatchingRisingEdgeEvents_List = list()

    global JOYSTICK_MostRecentDict_Joystick_Ball_Value_List
    JOYSTICK_MostRecentDict_Joystick_Ball_Value_List = list()

    global JOYSTICK_MostRecentDict_DataStreamingFrequency
    JOYSTICK_MostRecentDict_DataStreamingFrequency = -11111.0

    global JOYSTICK_MostRecentDict_Time
    JOYSTICK_MostRecentDict_Time = -11111.0
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_ReubenPython2and3ClassObject

    global MYPRINT_OPEN_FLAG
    MYPRINT_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################  KEY GUI LINE
    #################################################
    if USE_GUI_FLAG == 1:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  #Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        root = None
        Tab_MainControls = None
        Tab_JOYSTICK = None
        Tab_MyPrint = None
    #################################################
    #################################################

    #################################################
    #################################################

    ########################
    Joystick_NameDesired = "VKBsim Gladiator" #"" means that we don't care about the name.
    Joystick_IntegerIDdesired = -1 #-1 means that we don't care about the IntegerID.
    Joystick_ShowJustDotMovingFlag = 0
    Joystick_Axis_Index_ToDisplayAsHorizontalAxisOn2DdotDisplay = 0
    Joystick_Axis_Index_ToDisplayAsVerticalAxisOn2DdotDisplay = 1
    Joystick_Button_Index_ToDisplayAsDotColorOn2DdotDisplay = 13
    Joystick_PrintInfoForAllDetectedJoysticksFlag = 1
    ########################

    global JoystickHID_ReubenPython2and3ClassObject_GUIparametersDict
    JoystickHID_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_JOYSTICK_FLAG),
                                    ("root", Tab_JOYSTICK),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_JOYSTICK),
                                    ("GUI_COLUMN", GUI_COLUMN_JOYSTICK),
                                    ("GUI_PADX", GUI_PADX_JOYSTICK),
                                    ("GUI_PADY", GUI_PADY_JOYSTICK),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_JOYSTICK),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_JOYSTICK)])

    global JoystickHID_ReubenPython2and3ClassObject_setup_dict
    JoystickHID_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", JoystickHID_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                ("NameToDisplay_UserSet", "Reuben's JoystickHID_ReubenPython2and3Class Test"),
                                                                ("Joystick_NameDesired", Joystick_NameDesired),
                                                                ("Joystick_IntegerIDdesired", Joystick_IntegerIDdesired),
                                                                ("Joystick_ShowJustDotMovingFlag", Joystick_ShowJustDotMovingFlag),
                                                                ("Joystick_Axis_Index_ToDisplayAsHorizontalAxisOn2DdotDisplay", Joystick_Axis_Index_ToDisplayAsHorizontalAxisOn2DdotDisplay),
                                                                ("Joystick_Axis_Index_ToDisplayAsVerticalAxisOn2DdotDisplay", Joystick_Axis_Index_ToDisplayAsVerticalAxisOn2DdotDisplay),
                                                                ("Joystick_Button_Index_ToDisplayAsDotColorOn2DdotDisplay", Joystick_Button_Index_ToDisplayAsDotColorOn2DdotDisplay),
                                                                ("MainThread_TimeToSleepEachLoop", 0.010),
                                                                ("Joystick_PrintInfoForAllDetectedJoysticksFlag", Joystick_PrintInfoForAllDetectedJoysticksFlag)])

    if USE_JOYSTICK_FLAG == 1:
        try:
            JoystickHID_ReubenPython2and3ClassObject = JoystickHID_ReubenPython2and3Class(JoystickHID_ReubenPython2and3ClassObject_setup_dict)
            JOYSTICK_OPEN_FLAG = JoystickHID_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("JoystickHID_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1:

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MYPRINT_FLAG),
                                                                        ("root", Tab_MyPrint),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MYPRINT),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MYPRINT),
                                                                        ("GUI_PADX", GUI_PADX_MYPRINT),
                                                                        ("GUI_PADY", GUI_PADY_MYPRINT),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MYPRINT),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MYPRINT)])

        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            MYPRINT_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_JOYSTICK_FLAG == 1 and JOYSTICK_OPEN_FLAG != 1:
        print("Failed to open JoystickHID_ReubenPython2and3Class.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MYPRINT_FLAG == 1 and MYPRINT_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
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
        if JOYSTICK_OPEN_FLAG == 1:

            JOYSTICK_MostRecentDict = JoystickHID_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "Time" in JOYSTICK_MostRecentDict:
                JOYSTICK_MostRecentDict_Joystick_Axis_Value_List = JOYSTICK_MostRecentDict["Joystick_Axis_Value_List"]
                JOYSTICK_MostRecentDict_Joystick_Button_Value_List = JOYSTICK_MostRecentDict["Joystick_Button_Value_List"]
                JOYSTICK_MostRecentDict_Joystick_Button_LatchingRisingEdgeEvents_List = JOYSTICK_MostRecentDict["Joystick_Button_LatchingRisingEdgeEvents_List"]
                JOYSTICK_MostRecentDict_Joystick_Hat_Value_List = JOYSTICK_MostRecentDict["Joystick_Hat_Value_List"]
                JOYSTICK_MostRecentDict_Joystick_Hat_LatchingRisingEdgeEvents_List = JOYSTICK_MostRecentDict["Joystick_Hat_LatchingRisingEdgeEvents_List"]
                JOYSTICK_MostRecentDict_Joystick_Ball_Value_List = JOYSTICK_MostRecentDict["Joystick_Ball_Value_List"]
                JOYSTICK_MostRecentDict_DataStreamingFrequency = JOYSTICK_MostRecentDict["DataStreamingFrequency"]
                JOYSTICK_MostRecentDict_Time = JOYSTICK_MostRecentDict["Time"]

                #print("JOYSTICK_MostRecentDict: " + str(JOYSTICK_MostRecentDict))
                #print("JOYSTICK_MostRecentDict_Joystick_Axis_Value_List: " + str(JOYSTICK_MostRecentDict_Joystick_Axis_Value_List))
        ###################################################
        ###################################################

        ################################################### SET's
        ###################################################
        if JOYSTICK_OPEN_FLAG == 1 and (CurrentTime_MainLoopThread - ResetLatchedValuesTime >= 5.0):
            JoystickHID_ReubenPython2and3ClassObject.ResetButtonRisingEdgeEventLatch(13)
            JoystickHID_ReubenPython2and3ClassObject.ResetButtonRisingEdgeEventLatch(17)
            JoystickHID_ReubenPython2and3ClassObject.ResetHatRisingEdgeEventLatch(0, 0)
            JoystickHID_ReubenPython2and3ClassObject.ResetHatRisingEdgeEventLatch(0, 1)
            ResetLatchedValuesTime = CurrentTime_MainLoopThread
        ###################################################
        ###################################################

        time.sleep(0.002)
    #################################################
    #################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_JoystickHID_ReubenPython2and3Class.")

    #################################################
    if JOYSTICK_OPEN_FLAG == 1:
        JoystickHID_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if MYPRINT_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

##########################################################################################################
##########################################################################################################