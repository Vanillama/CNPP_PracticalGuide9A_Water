import tkinter as tk
import numpy as np
from tkinter import ttk
from PIL import Image, ImageTk
import industrialBuilding as indB


### Colours ###
hydrogainBlue  = "#263A91"
hydrogainGreen = "#A1CA18"



##### Industrial Building window initialisation #####
def industrialBuildingWindow(rootWindow, screenWidth, screenHeight):
    
    industrialBuildingWindow = tk.Toplevel(rootWindow)
    industrialBuildingWindow.title("CNPP Practical Guide - Industrial Building")
    #industrialBuildingWindow.iconbitmap("Resources/Images/HydroGainLogo_NoText.ico")
    industrialBuildingWindow.iconbitmap("Resources/Images/CNPPLogo_Simple.ico")
    industrialBuildingWindow.geometry(str(int(screenWidth*1.2)) + "x" + str(int(screenHeight*1.2)))
    
    industrialBuildingWindow.rowconfigure(0, weight = 1)
    industrialBuildingWindow.rowconfigure(1, weight = 1)
    industrialBuildingWindow.rowconfigure(2, weight = 1)
    industrialBuildingWindow.rowconfigure(3, weight = 1)
    industrialBuildingWindow.rowconfigure(4, weight = 1)
    industrialBuildingWindow.rowconfigure(5, weight = 1)
    industrialBuildingWindow.rowconfigure(6, weight = 1)
    industrialBuildingWindow.rowconfigure(7, weight = 1)
    industrialBuildingWindow.rowconfigure(8, weight = 1)
    industrialBuildingWindow.rowconfigure(9, weight = 1)
    
    industrialBuildingWindow.columnconfigure(0, weight = 1)
    industrialBuildingWindow.columnconfigure(1, weight = 1)
    industrialBuildingWindow.columnconfigure(2, weight = 5)
    
    
    ##############################
    
    
    ### FUNCTIONS ###
    industrialBuildingObjects = []
    industrialBuildingObjectValue = {
        "heightCoef" : 0.0,
        "fireResistanceCoef" : 0.0,
        "hazardousMaterialCoef" : 0.0,
        "internalInterventionTypeCoef" : 0.0,
        "sumCoef1" : 0.0,
        "sumCoef2" : 0.0,
        "intermFlowRate" : 0.0,
        "riskCategoryCoef" : 0.0,
        "autoWaterExtinctCoef" : 0.0}
    
    
    ##############################
    
    
    ### Row 0 ###
    industrialClassTitle = ttk.Label(industrialBuildingWindow, text = "Industrial building", font = ("TkDefaultFont", 20, "bold"), foreground = hydrogainBlue)
    industrialClassTitle.grid(row = 0, column = 0, columnspan = 10)
    
    
    
    
    
    
    
    
    