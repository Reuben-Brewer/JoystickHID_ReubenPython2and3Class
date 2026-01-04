# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision N, 12/27/2025

Verified working on: Python 3.11/12/13 for Windows 10/11 64-bit, Ubuntu 20.04, and Raspberry Pi 4/5.
'''

__author__ = 'reuben.brewer'

##########################################################################################################
##########################################################################################################

#################################################
import os
import sys
import platform
import time, datetime
import math
import collections
import inspect #To enable 'TellWhichFileWereIn'
import threading
import queue as Queue
import traceback
#################################################

#################################################
from tkinter import *
import tkinter.font as tkFont
from tkinter import ttk
#################################################

#################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#################################################

##########################################################################################################
##########################################################################################################

class Joystick2DdotDisplay_ReubenPython2and3Class(Frame): #Subclass the Tkinter Frame

    #######################################################################################################################
    #######################################################################################################################
    def __init__(self, setup_dict): #Subclass the Tkinter Frame

        print("#################### Joystick2DdotDisplay_ReubenPython2and3Class __init__ starting. ####################")

        #########################################################
        #########################################################
        self.GUI_ready_to_be_updated_flag = 0
        self.OBJECT_CREATED_SUCCESSFULLY_FLAG = -1

        self.Input_Xvalue = 0
        self.Input_Yvalue = 0
        self.DotHighlightedLikeButtonPress_State = 0
        
        self.ListOfAcceptableColorsEnglishNameStrings = ["Red", "Blue", "Green", "Yellow", "Orange", "Black", "Gray", "Purple"]
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if platform.system() == "Linux":

            if "raspberrypi" in platform.uname(): #os.uname() doesn't work in windows
                self.my_platform = "pi"
            else:
                self.my_platform = "linux"

        elif platform.system() == "Windows":
            self.my_platform = "windows"

        elif platform.system() == "Darwin":
            self.my_platform = "mac"

        else:
            self.my_platform = "other"

        print("Joystick2DdotDisplay_ReubenPython2and3Class __init__: The OS platform is: " + self.my_platform)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "GUIparametersDict" in setup_dict:
            self.GUIparametersDict = setup_dict["GUIparametersDict"]

            ##########################################
            if "GUI_ROW" in self.GUIparametersDict:
                self.GUI_ROW = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROW", self.GUIparametersDict["GUI_ROW"], 0.0, 1000.0))
            else:
                self.GUI_ROW = 0

            print("Joystick2DdotDisplay_ReubenPython2and3Class __init__: GUI_ROW: " + str(self.GUI_ROW))
            ##########################################

            ##########################################
            if "GUI_COLUMN" in self.GUIparametersDict:
                self.GUI_COLUMN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMN", self.GUIparametersDict["GUI_COLUMN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMN = 0

            print("Joystick2DdotDisplay_ReubenPython2and3Class __init__: GUI_COLUMN: " + str(self.GUI_COLUMN))
            ##########################################

            ##########################################
            if "GUI_PADX" in self.GUIparametersDict:
                self.GUI_PADX = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADX", self.GUIparametersDict["GUI_PADX"], 0.0, 1000.0))
            else:
                self.GUI_PADX = 0

            print("Joystick2DdotDisplay_ReubenPython2and3Class __init__: GUI_PADX: " + str(self.GUI_PADX))
            ##########################################

            ##########################################
            if "GUI_PADY" in self.GUIparametersDict:
                self.GUI_PADY = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADY", self.GUIparametersDict["GUI_PADY"], 0.0, 1000.0))
            else:
                self.GUI_PADY = 0

            print("Joystick2DdotDisplay_ReubenPython2and3Class __init__: GUI_PADY: " + str(self.GUI_PADY))
            ##########################################

            ##########################################
            if "GUI_ROWSPAN" in self.GUIparametersDict:
                self.GUI_ROWSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROWSPAN", self.GUIparametersDict["GUI_ROWSPAN"], 0.0, 1000.0))
            else:
                self.GUI_ROWSPAN = 1

            print("Joystick2DdotDisplay_ReubenPython2and3Class __init__: GUI_ROWSPAN: " + str(self.GUI_ROWSPAN))
            ##########################################

            ##########################################
            if "GUI_COLUMNSPAN" in self.GUIparametersDict:
                self.GUI_COLUMNSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMNSPAN", self.GUIparametersDict["GUI_COLUMNSPAN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMNSPAN = 1

            print("Joystick2DdotDisplay_ReubenPython2and3Class __init__: GUI_COLUMNSPAN: " + str(self.GUI_COLUMNSPAN))
            ##########################################

            ##########################################
            if "GUI_STICKY" in self.GUIparametersDict:
                self.GUI_STICKY = str(self.GUIparametersDict["GUI_STICKY"])
            else:
                self.GUI_STICKY = "w"

            print("Joystick2DdotDisplay_ReubenPython2and3Class __init__: GUI_STICKY: " + str(self.GUI_STICKY))
            ##########################################

        else:
            self.GUIparametersDict = dict()
            self.USE_GUI_FLAG = 0
            print("Joystick2DdotDisplay_ReubenPython2and3Class __init__: No GUIparametersDict present, setting USE_GUI_FLAG: " + str(self.USE_GUI_FLAG))

        #print("GUIparametersDict = " + str(self.GUIparametersDict))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "JoystickXYboxCanvas_HeightAndWidth" in setup_dict:
            self.JoystickXYboxCanvas_HeightAndWidth = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("JoystickXYboxCanvas_HeightAndWidth", setup_dict["JoystickXYboxCanvas_HeightAndWidth"], 100.0, 1000.0))
        else:
            self.JoystickXYboxCanvas_HeightAndWidth = 150

        print("Joystick2DdotDisplay_ReubenPython2and3Class __init__: JoystickXYboxCanvas_HeightAndWidth: " + str(self.JoystickXYboxCanvas_HeightAndWidth))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "JoystickXYboxCanvas_FontSize" in setup_dict:
            self.JoystickXYboxCanvas_FontSize = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("JoystickXYboxCanvas_FontSize", setup_dict["JoystickXYboxCanvas_FontSize"], 8.0, 100.0))
        else:
            self.JoystickXYboxCanvas_FontSize = 12

        print("Joystick2DdotDisplay_ReubenPython2and3Class __init__: JoystickXYboxCanvas_FontSize: " + str(self.JoystickXYboxCanvas_FontSize))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.ProcessSetupDictInputsTheCanBeLiveChanged(setup_dict)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.OBJECT_CREATED_SUCCESSFULLY_FLAG = 1
        #########################################################
        #########################################################

    #######################################################################################################################
    #######################################################################################################################

    #######################################################################################################################
    #######################################################################################################################
    def ProcessSetupDictInputsTheCanBeLiveChanged(self, setup_dict):

        #########################################################
        #########################################################
        if "NameToDisplay_UserSet" in setup_dict:
            self.NameToDisplay_UserSet = str(setup_dict["NameToDisplay_UserSet"])
        else:
            self.NameToDisplay_UserSet = ""

        print("Joystick2DdotDisplay_ReubenPython2and3Class ProcessSetupDictInputsTheCanBeLiveChanged: NameToDisplay_UserSet: " + str(self.NameToDisplay_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MaxValue" in setup_dict:
            self.MaxValue = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("MaxValue", setup_dict["MaxValue"], 0.0, 1000000.0)
        else:
            self.MaxValue = 1.0

        print("Joystick2DdotDisplay_ReubenPython2and3Class ProcessSetupDictInputsTheCanBeLiveChanged: MaxValue: " + str(self.MaxValue))

        self.X_min = -1.0*self.MaxValue
        self.X_max = self.MaxValue

        self.Y_min = -1.0*self.MaxValue
        self.Y_max = self.MaxValue
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Crosshairs_ShowFlag" in setup_dict:
            self.Crosshairs_ShowFlag = self.PassThrough0and1values_ExitProgramOtherwise("Crosshairs_ShowFlag", setup_dict["Crosshairs_ShowFlag"])
        else:
            self.Crosshairs_ShowFlag = 0

        print("Joystick2DdotDisplay_ReubenPython2and3Class ProcessSetupDictInputsTheCanBeLiveChanged: Crosshairs_ShowFlag: " + str(self.Crosshairs_ShowFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Crosshairs_VerticalLine_Xvalue" in setup_dict:
            self.Crosshairs_VerticalLine_Xvalue = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Crosshairs_VerticalLine_Xvalue", setup_dict["Crosshairs_VerticalLine_Xvalue"], -1.0*self.MaxValue, 1.0*self.MaxValue)
        else:
            self.Crosshairs_VerticalLine_Xvalue = 0.0

        print("Joystick2DdotDisplay_ReubenPython2and3Class ProcessSetupDictInputsTheCanBeLiveChanged: Crosshairs_VerticalLine_Xvalue: " + str(self.Crosshairs_VerticalLine_Xvalue))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Crosshairs_HorizontalLine_Yvalue" in setup_dict:
            self.Crosshairs_HorizontalLine_Yvalue = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Crosshairs_HorizontalLine_Yvalue", setup_dict["Crosshairs_HorizontalLine_Yvalue"], -1.0*self.MaxValue, 1.0*self.MaxValue)
        else:
            self.Crosshairs_HorizontalLine_Yvalue = 0.0

        print("Joystick2DdotDisplay_ReubenPython2and3Class ProcessSetupDictInputsTheCanBeLiveChanged: Crosshairs_HorizontalLine_Yvalue: " + str(self.Crosshairs_HorizontalLine_Yvalue))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "CircularBoundary_Radius" in setup_dict:
            self.CircularBoundary_Radius = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("CircularBoundary_Radius", setup_dict["CircularBoundary_Radius"], 0.0, 1.0*self.MaxValue)
        else:
            self.CircularBoundary_Radius = 0.0

        print("Joystick2DdotDisplay_ReubenPython2and3Class ProcessSetupDictInputsTheCanBeLiveChanged: CircularBoundary_Radius: " + str(self.CircularBoundary_Radius))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ExtendMarkerRadiallyToOriginFlag" in setup_dict:
            self.ExtendMarkerRadiallyToOriginFlag = self.PassThrough0and1values_ExitProgramOtherwise("ExtendMarkerRadiallyToOriginFlag", setup_dict["ExtendMarkerRadiallyToOriginFlag"])
        else:
            self.ExtendMarkerRadiallyToOriginFlag = 0

        print("Joystick2DdotDisplay_ReubenPython2and3Class ProcessSetupDictInputsTheCanBeLiveChanged: ExtendMarkerRadiallyToOriginFlag: " + str(self.ExtendMarkerRadiallyToOriginFlag))
        #########################################################
        #########################################################
        
        #########################################################
        #########################################################
        if "PointerColor_Unhighlighted" in setup_dict:
            PointerColor_Unhighlighted_temp = setup_dict["PointerColor_Unhighlighted"]

            #########################################################
            if PointerColor_Unhighlighted_temp in self.ListOfAcceptableColorsEnglishNameStrings:
                self.PointerColor_Unhighlighted = PointerColor_Unhighlighted_temp
            #########################################################

            #########################################################
            else:
                print("Joystick2DdotDisplay_ReubenPython2and3Class: Error, PointerColor_Unhighlighted must be in " + str(self.ListOfAcceptableColorsEnglishNameStrings))
                self.PointerColor_Unhighlighted = "Red"
            #########################################################
            
        else:
            self.PointerColor_Unhighlighted = "Red"

        print("Joystick2DdotDisplay_ReubenPython2and3Class ProcessSetupDictInputsTheCanBeLiveChanged: PointerColor_Unhighlighted: " + str(self.PointerColor_Unhighlighted))
        #########################################################
        #########################################################
        
        #########################################################
        #########################################################
        if "PointerColor_Highlighted" in setup_dict:
            PointerColor_Highlighted_temp = setup_dict["PointerColor_Highlighted"]

            #########################################################
            if PointerColor_Highlighted_temp in self.ListOfAcceptableColorsEnglishNameStrings:
                self.PointerColor_Highlighted = PointerColor_Highlighted_temp
            #########################################################

            #########################################################
            else:
                print("Joystick2DdotDisplay_ReubenPython2and3Class: Error, PointerColor_Highlighted must be in " + str(self.ListOfAcceptableColorsEnglishNameStrings))
                self.PointerColor_Highlighted = "Green"
            #########################################################
            
        else:
            self.PointerColor_Highlighted = "Green"

        print("Joystick2DdotDisplay_ReubenPython2and3Class ProcessSetupDictInputsTheCanBeLiveChanged: PointerColor_Highlighted: " + str(self.PointerColor_Highlighted))
        #########################################################
        #########################################################

    #######################################################################################################################
    #######################################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def CreateGUIobjects(self, TkinterParent):

        print("Joystick2DdotDisplay_ReubenPython2and3Class, CreateGUIobjects event fired.")

        #################################################
        #################################################
        self.root = TkinterParent
        self.parent = TkinterParent
        #################################################
        #################################################

        #########################################################
        #########################################################
        self.myFrame = Frame(self.root)

        self.myFrame.grid(row = self.GUI_ROW,
                          column = self.GUI_COLUMN,
                          padx = self.GUI_PADX,
                          pady = self.GUI_PADY,
                          rowspan = self.GUI_ROWSPAN,
                          columnspan= self.GUI_COLUMNSPAN,
                          sticky = self.GUI_STICKY)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.JoystickXYboxCanvas_BorderWidth = 1
        self.JoystickXYboxCanvas_PointerCircle_Radius = 5
        self.JoystickXYboxCanvas_PointerLine_Width = 1.2*2.0*self.JoystickXYboxCanvas_PointerCircle_Radius

        ######################################################### Create and draw canvas
        self.JoystickXYboxCanvas = Canvas(self.myFrame,
                                         width=self.JoystickXYboxCanvas_HeightAndWidth,
                                         height=self.JoystickXYboxCanvas_HeightAndWidth) #bg="white", highlightbackground="black"

        self.JoystickXYboxCanvas["highlightthickness"] = 0  #IMPORTANT Remove light grey border around the Canvas
        self.JoystickXYboxCanvas["bd"] = 0 #IMPORTANT Setting "bd", along with "highlightthickness" to 0 makes the Canvas be in the (0,0) pixel location instead of offset by those thicknesses
        self.JoystickXYboxCanvas.grid(row=0, column=0, padx=0, pady=0, columnspan=1, rowspan=1)
        #########################################################

        ######################################################### Create black outline around canvas
        self.JoystickXYboxCanvas.create_rectangle(0.5*self.JoystickXYboxCanvas_BorderWidth,
                                                0.5 * self.JoystickXYboxCanvas_BorderWidth,
                                                self.JoystickXYboxCanvas_HeightAndWidth - 0.5 * self.JoystickXYboxCanvas_BorderWidth -1, #The -1 accounts for indexing at 0
                                                self.JoystickXYboxCanvas_HeightAndWidth - 0.5 * self.JoystickXYboxCanvas_BorderWidth -1, #The -1 accounts for indexing at 0
                                                outline="black",
                                                fill="white",
                                                width=self.JoystickXYboxCanvas_BorderWidth,
                                                tags='BorderRectangle_Tag')
        #########################################################

        ######################################################### Create cicle
        self.JoystickXYboxCanvas_PointerCircle = self.CreateAndDrawCircleOnCanvas_CanvasCoord(self.JoystickXYboxCanvas, 0, 0, self.JoystickXYboxCanvas_PointerCircle_Radius, self.PointerColor_Unhighlighted)
        #########################################################

        #########################################################
        self.DebuggingInfo_Label = Label(self.myFrame, text="DebuggingInfo_Label", font=("Helvetica", self.JoystickXYboxCanvas_FontSize))
        self.DebuggingInfo_Label.grid(row=1, column=0, padx=1, pady=1, columnspan=1, rowspan=1)
        #########################################################

        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.GUI_ready_to_be_updated_flag = 1
        #########################################################
        #########################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def LimitNumber_FloatOutputOnly(self, min_val, max_val, test_val):
        if test_val > max_val:
            test_val = max_val

        elif test_val < min_val:
            test_val = min_val

        else:
            test_val = test_val

        test_val = float(test_val)

        return test_val
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    def PassThrough0and1values_ExitProgramOtherwise(self, InputNameString, InputNumber, ExitProgramIfFailureFlag = 0):

        ##########################################################################################################
        ##########################################################################################################
        try:

            ##########################################################################################################
            InputNumber_ConvertedToFloat = float(InputNumber)
            ##########################################################################################################

        except:

            ##########################################################################################################
            exceptions = sys.exc_info()[0]
            print(self.TellWhichFileWereIn() + ", PassThrough0and1values_ExitProgramOtherwise Error. InputNumber '" + InputNameString + "' must be a numerical value, Exceptions: %s" % exceptions)

            ##########################
            if ExitProgramIfFailureFlag == 1:
                sys.exit()
            else:
                return -1
            ##########################

            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        try:

            ##########################################################################################################
            if InputNumber_ConvertedToFloat == 0.0 or InputNumber_ConvertedToFloat == 1.0:
                return InputNumber_ConvertedToFloat

            else:

                print(self.TellWhichFileWereIn() + ", PassThrough0and1values_ExitProgramOtherwise Error. '" +
                              str(InputNameString) +
                              "' must be 0 or 1 (value was " +
                              str(InputNumber_ConvertedToFloat) +
                              "). Press any key (and enter) to exit.")

                ##########################
                if ExitProgramIfFailureFlag == 1:
                    sys.exit()

                else:
                    return -1
                ##########################

            ##########################################################################################################

        except:

            ##########################################################################################################
            exceptions = sys.exc_info()[0]
            print(self.TellWhichFileWereIn() + ", PassThrough0and1values_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)

            ##########################
            if ExitProgramIfFailureFlag == 1:
                sys.exit()
            else:
                return -1
            ##########################

            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    def PassThroughFloatValuesInRange_ExitProgramOtherwise(self, InputNameString, InputNumber, RangeMinValue, RangeMaxValue, ExitProgramIfFailureFlag = 0):

        ##########################################################################################################
        ##########################################################################################################
        try:
            ##########################################################################################################
            InputNumber_ConvertedToFloat = float(InputNumber)
            ##########################################################################################################

        except:
            ##########################################################################################################
            exceptions = sys.exc_info()[0]
            print(self.TellWhichFileWereIn() + ", PassThroughFloatValuesInRange_ExitProgramOtherwise Error. InputNumber '" + InputNameString + "' must be a float value, Exceptions: %s" % exceptions)
            traceback.print_exc()

            ##########################
            if ExitProgramIfFailureFlag == 1:
                sys.exit()
            else:
                return -11111.0
            ##########################

            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        try:

            ##########################################################################################################
            InputNumber_ConvertedToFloat_Limited = self.LimitNumber_FloatOutputOnly(RangeMinValue, RangeMaxValue, InputNumber_ConvertedToFloat)

            if InputNumber_ConvertedToFloat_Limited != InputNumber_ConvertedToFloat:
                print(self.TellWhichFileWereIn() + ", PassThroughFloatValuesInRange_ExitProgramOtherwise Error. '" +
                      str(InputNameString) +
                      "' must be in the range [" +
                      str(RangeMinValue) +
                      ", " +
                      str(RangeMaxValue) +
                      "] (value was " +
                      str(InputNumber_ConvertedToFloat) + ")")

                ##########################
                if ExitProgramIfFailureFlag == 1:
                    sys.exit()
                else:
                    return -11111.0
                ##########################

            else:
                return InputNumber_ConvertedToFloat_Limited
            ##########################################################################################################

        except:
            ##########################################################################################################
            exceptions = sys.exc_info()[0]
            print(self.TellWhichFileWereIn() + ", PassThroughFloatValuesInRange_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
            traceback.print_exc()

            ##########################
            if ExitProgramIfFailureFlag == 1:
                sys.exit()
            else:
                return -11111.0
            ##########################

            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def TellWhichFileWereIn(self):

        #We used to use this method, but it gave us the root calling file, not the class calling file
        #absolute_file_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        #filename = absolute_file_path[absolute_file_path.rfind("\\") + 1:]

        frame = inspect.stack()[1]
        filename = frame[1][frame[1].rfind("\\") + 1:]
        filename = filename.replace(".py","")

        return filename
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateDotCoordinatesAndDotColor(self, X, Y, DotHighlightedLikeButtonPress_State = 0):
        self.Input_Xvalue = self.LimitNumber_FloatOutputOnly(self.X_min, self.X_max, X)
        self.Input_Yvalue = self.LimitNumber_FloatOutputOnly(self.Y_min, self.Y_max, Y)

        if DotHighlightedLikeButtonPress_State in [0, 1]:
            self.DotHighlightedLikeButtonPress_State = DotHighlightedLikeButtonPress_State
        else:
            self.DotHighlightedLikeButtonPress_State = 0

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def CreateAndDrawCircleOnCanvas_CanvasCoord(self, myCanvas, CenterX_CanvasCoord, CenterY_CanvasCoord, Radius, Color = "black"):

        CircleBoundingBoxCoordinates_CanvasCoord = self.GetCircleBoundingBoxCoordinatesListOnCanvas_CanvasCoord(CenterX_CanvasCoord, CenterY_CanvasCoord, Radius)

        CircleObjectToReturn = myCanvas.create_oval(CircleBoundingBoxCoordinates_CanvasCoord[0],
                                                    CircleBoundingBoxCoordinates_CanvasCoord[1],
                                                    CircleBoundingBoxCoordinates_CanvasCoord[2],
                                                    CircleBoundingBoxCoordinates_CanvasCoord[3],
                                                    outline=Color,
                                                    fill=Color,
                                                    width=0,
                                                    tags="CircleOnCanvas_Tag")
        return CircleObjectToReturn
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GetCircleBoundingBoxCoordinatesListOnCanvas_CanvasCoord(self, CenterX_CanvasCoord, CenterY_CanvasCoord, Radius):

        coordinates_list = [CenterX_CanvasCoord - Radius,
                            CenterY_CanvasCoord - Radius,
                            CenterX_CanvasCoord + Radius,
                            CenterY_CanvasCoord + Radius]

        return coordinates_list
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ConvertMathPointToJoystickCanvasCoordinates(self, PointListXY):

        ####
        x = PointListXY[0]
        y = PointListXY[1]

        W = self.JoystickXYboxCanvas_HeightAndWidth
        H = self.JoystickXYboxCanvas_HeightAndWidth

        GraphBoxOutline_X0 = 0
        GraphBoxOutline_Y0 = 0
        ####

        ####
        m_Xaxis = ((W - GraphBoxOutline_X0)/(self.X_max - self.X_min))
        b_Xaxis = W - m_Xaxis*self.X_max

        X_out = m_Xaxis*x + b_Xaxis
        ####

        ####
        m_Yaxis = ((H - GraphBoxOutline_Y0) / (self.Y_max - self.Y_min))
        b_Yaxis = H - m_Yaxis * self.Y_max

        Y_out = m_Yaxis * y + b_Yaxis
        ####

        ####
        X_out = X_out
        Y_out = self.JoystickXYboxCanvas.winfo_height() - Y_out #Flip y-axis
        ####

        return [X_out, Y_out]
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GUI_update_clock(self):

            #######################################################
            #######################################################
            #######################################################
            if self.GUI_ready_to_be_updated_flag == 1:

                #######################################################
                #######################################################
                try:

                    ### Debug drawing functions
                    #self.CreateAndDrawCircleOnCanvas_CanvasCoord(self.JoystickXYboxCanvas, 0, 0, self.JoystickXYboxCanvas_PointerCircle_Radius, "green") #ONLY A TESTING LINE
                    #PointCoords_CanvasCoord = self.ConvertMathPointToJoystickCanvasCoordinates([0, 0])
                    #PointCoords_CanvasCoord = self.ConvertMathPointToJoystickCanvasCoordinates([0, 1])
                    #PointCoords_CanvasCoord = self.ConvertMathPointToJoystickCanvasCoordinates([1, 1])
                    ### Debug drawing functions

                    #######################################################
                    if self.DotHighlightedLikeButtonPress_State == 1:
                        ColorToUse = self.PointerColor_Highlighted
                    else:
                        ColorToUse = self.PointerColor_Unhighlighted
                    #######################################################

                    #######################################################
                    PointCoords_CanvasCoord = self.ConvertMathPointToJoystickCanvasCoordinates([self.Input_Xvalue, self.Input_Yvalue])

                    CircleBoundingBoxCoordinates_CanvasCoord = self.GetCircleBoundingBoxCoordinatesListOnCanvas_CanvasCoord(PointCoords_CanvasCoord[0],
                                                                                                                           PointCoords_CanvasCoord[1],
                                                                                                                           self.JoystickXYboxCanvas_PointerCircle_Radius)

                    self.JoystickXYboxCanvas.coords(self.JoystickXYboxCanvas_PointerCircle,
                                                       CircleBoundingBoxCoordinates_CanvasCoord[0],
                                                       CircleBoundingBoxCoordinates_CanvasCoord[1],
                                                       CircleBoundingBoxCoordinates_CanvasCoord[2],
                                                       CircleBoundingBoxCoordinates_CanvasCoord[3])

                    self.JoystickXYboxCanvas.itemconfig(self.JoystickXYboxCanvas_PointerCircle, fill=ColorToUse, outline=ColorToUse)
                    #######################################################

                    #######################################################
                    self.DebuggingInfo_Label["text"] = self.NameToDisplay_UserSet + " " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput([self.Input_Xvalue, self.Input_Yvalue], 0, 3)
                    #######################################################

                    #######################################################
                    if self.ExtendMarkerRadiallyToOriginFlag == 1:
                        PointerLineCoords_Origin_CanvasCoord = self.ConvertMathPointToJoystickCanvasCoordinates([0.0, 0.0])

                        self.JoystickXYboxCanvas.delete("PointerLine_tag")
                        self.JoystickXYboxCanvas.create_line(PointerLineCoords_Origin_CanvasCoord[0] + 1 * self.JoystickXYboxCanvas_BorderWidth,  # Don't cross the border
                                                             PointerLineCoords_Origin_CanvasCoord[1],
                                                             PointCoords_CanvasCoord[0] - 1 * self.JoystickXYboxCanvas_BorderWidth,  # Don't cross the border
                                                             PointCoords_CanvasCoord[1],
                                                             fill=ColorToUse,
                                                             width=self.JoystickXYboxCanvas_PointerLine_Width,
                                                             tags="PointerLine_tag")  # dash=(10)
                    #######################################################

                    #######################################################
                    if self.Crosshairs_ShowFlag == 1:

                        HorizontalLineCoords_LeftOfLine_CanvasCoord = self.ConvertMathPointToJoystickCanvasCoordinates([self.X_min, self.Crosshairs_HorizontalLine_Yvalue])
                        HorizontalLineCoords_RightOfLine_CanvasCoord = self.ConvertMathPointToJoystickCanvasCoordinates([self.X_max, self.Crosshairs_HorizontalLine_Yvalue])

                        VerticalLineCoords_BottomOfLine_CanvasCoord = self.ConvertMathPointToJoystickCanvasCoordinates([self.Crosshairs_VerticalLine_Xvalue, self.Y_min])
                        VerticalLineCoords_TopOfLine_CanvasCoord = self.ConvertMathPointToJoystickCanvasCoordinates([self.Crosshairs_VerticalLine_Xvalue, self.Y_max])

                        self.JoystickXYboxCanvas.delete("HorizontalLine_tag")
                        self.JoystickXYboxCanvas.create_line(HorizontalLineCoords_LeftOfLine_CanvasCoord[0] + 1*self.JoystickXYboxCanvas_BorderWidth, #Don't cross the border
                                                             HorizontalLineCoords_LeftOfLine_CanvasCoord[1],
                                                             HorizontalLineCoords_RightOfLine_CanvasCoord[0] - 1*self.JoystickXYboxCanvas_BorderWidth, #Don't cross the border
                                                             HorizontalLineCoords_RightOfLine_CanvasCoord[1],
                                                             fill="black",
                                                             width=1,
                                                             dash=5,
                                                             tags="HorizontalLine_tag") #dash=(10)

                        self.JoystickXYboxCanvas.delete("VerticalLine_tag")
                        self.JoystickXYboxCanvas.create_line(VerticalLineCoords_BottomOfLine_CanvasCoord[0],
                                                             VerticalLineCoords_BottomOfLine_CanvasCoord[1] - 1*self.JoystickXYboxCanvas_BorderWidth, #Don't cross the border
                                                             VerticalLineCoords_TopOfLine_CanvasCoord[0],
                                                             VerticalLineCoords_TopOfLine_CanvasCoord[1] + 1*self.JoystickXYboxCanvas_BorderWidth, #Don't cross the border
                                                             fill="black",
                                                             width=1,
                                                             dash=5,
                                                             tags="VerticalLine_tag")
                    #######################################################

                    #######################################################
                    if self.CircularBoundary_Radius > 0.0:
                        CircularBoundary_CanvasCoord = self.ConvertMathPointToJoystickCanvasCoordinates([0.0, 0.0])

                        CircularBoundaryBoundingBoxCoordinates_CanvasCoord = self.GetCircleBoundingBoxCoordinatesListOnCanvas_CanvasCoord(CircularBoundary_CanvasCoord[0],
                                                                                                                                            CircularBoundary_CanvasCoord[1],
                                                                                                                                          (self.CircularBoundary_Radius/self.MaxValue)*self.JoystickXYboxCanvas_HeightAndWidth/2.0)

                        self.JoystickXYboxCanvas.delete("CircularBoundary_Tag")
                        self.JoystickXYboxCanvas.create_oval(CircularBoundaryBoundingBoxCoordinates_CanvasCoord[0],
                                                             CircularBoundaryBoundingBoxCoordinates_CanvasCoord[1],
                                                             CircularBoundaryBoundingBoxCoordinates_CanvasCoord[2],
                                                             CircularBoundaryBoundingBoxCoordinates_CanvasCoord[3],
                                                             outline="Black", #To have no fill, delete the line "fill="Black","
                                                             width=1,
                                                             dash=(5),
                                                             tags="CircularBoundary_Tag")
                    #######################################################


                except:
                    exceptions = sys.exc_info()[0]
                    print("Joystick2DdotDisplay_ReubenPython2and3Class GUI_update_clock, Exceptions: %s" % exceptions)
                    traceback.print_exc()
                #######################################################
                #######################################################

            #######################################################
            #######################################################
            #######################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    def ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self, input, number_of_leading_numbers = 4, number_of_decimal_places = 3):

        number_of_decimal_places = max(1, number_of_decimal_places) #Make sure we're above 1

        ListOfStringsToJoin = []

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        if isinstance(input, str) == 1:
            ListOfStringsToJoin.append(input)
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, int) == 1 or isinstance(input, float) == 1:
            element = float(input)
            prefix_string = "{:." + str(number_of_decimal_places) + "f}"
            element_as_string = prefix_string.format(element)

            ##########################################################################################################
            ##########################################################################################################
            if element >= 0:
                element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1)  # +1 for sign, +1 for decimal place
                element_as_string = "+" + element_as_string  # So that our strings always have either + or - signs to maintain the same string length
            else:
                element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1 + 1)  # +1 for sign, +1 for decimal place
            ##########################################################################################################
            ##########################################################################################################

            ListOfStringsToJoin.append(element_as_string)
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, list) == 1:

            if len(input) > 0:
                for element in input: #RECURSION
                    ListOfStringsToJoin.append(self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a list() or []
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, tuple) == 1:

            if len(input) > 0:
                for element in input: #RECURSION
                    ListOfStringsToJoin.append("TUPLE" + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a list() or []
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, dict) == 1:

            if len(input) > 0:
                for Key in input: #RECURSION
                    ListOfStringsToJoin.append(str(Key) + ": " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input[Key], number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a dict()
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        else:
            ListOfStringsToJoin.append(str(input))
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        if len(ListOfStringsToJoin) > 1:

            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            StringToReturn = ""
            for Index, StringToProcess in enumerate(ListOfStringsToJoin):

                ################################################
                if Index == 0: #The first element
                    if StringToProcess.find(":") != -1 and StringToProcess[0] != "{": #meaning that we're processing a dict()
                        StringToReturn = "{"
                    elif StringToProcess.find("TUPLE") != -1 and StringToProcess[0] != "(":  # meaning that we're processing a tuple
                        StringToReturn = "("
                    else:
                        StringToReturn = "["

                    StringToReturn = StringToReturn + StringToProcess.replace("TUPLE","") + ", "
                ################################################

                ################################################
                elif Index < len(ListOfStringsToJoin) - 1: #The middle elements
                    StringToReturn = StringToReturn + StringToProcess + ", "
                ################################################

                ################################################
                else: #The last element
                    StringToReturn = StringToReturn + StringToProcess

                    if StringToProcess.find(":") != -1 and StringToProcess[-1] != "}":  # meaning that we're processing a dict()
                        StringToReturn = StringToReturn + "}"
                    elif StringToProcess.find("TUPLE") != -1 and StringToProcess[-1] != ")":  # meaning that we're processing a tuple
                        StringToReturn = StringToReturn + ")"
                    else:
                        StringToReturn = StringToReturn + "]"

                ################################################

            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################

        elif len(ListOfStringsToJoin) == 1:
            StringToReturn = ListOfStringsToJoin[0]

        else:
            StringToReturn = ListOfStringsToJoin

        return StringToReturn
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ConvertDictToProperlyFormattedStringForPrinting(self, DictToPrint, NumberOfDecimalsPlaceToUse = 3, NumberOfEntriesPerLine = 1, NumberOfTabsBetweenItems = 3):

        try:
            ProperlyFormattedStringForPrinting = ""
            ItemsPerLineCounter = 0

            for Key in DictToPrint:

                ##########################################################################################################
                if isinstance(DictToPrint[Key], dict): #RECURSION
                    ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                         str(Key) + ":\n" + \
                                                         self.ConvertDictToProperlyFormattedStringForPrinting(DictToPrint[Key],
                                                                                                              NumberOfDecimalsPlaceToUse,
                                                                                                              NumberOfEntriesPerLine,
                                                                                                              NumberOfTabsBetweenItems)

                else:
                    ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                         str(Key) + ": " + \
                                                         self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(DictToPrint[Key],
                                                                                                                                               0,
                                                                                                                                               NumberOfDecimalsPlaceToUse)
                ##########################################################################################################

                ##########################################################################################################
                if ItemsPerLineCounter < NumberOfEntriesPerLine - 1:
                    ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\t"*NumberOfTabsBetweenItems
                    ItemsPerLineCounter = ItemsPerLineCounter + 1
                else:
                    ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\n"
                    ItemsPerLineCounter = 0
                ##########################################################################################################

            return ProperlyFormattedStringForPrinting

        except:
            exceptions = sys.exc_info()[0]
            print("ConvertDictToProperlyFormattedStringForPrinting, Exceptions: %s" % exceptions)
            return ""
            #traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################
