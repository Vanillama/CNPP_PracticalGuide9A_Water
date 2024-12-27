import tkinter as tk
import numpy as np
from tkinter import ttk
from PIL import Image, ImageTk
import residentialBuilding as rB


### Colours ###
hydrogainBlue  = "#263A91"
hydrogainGreen = "#A1CA18"



##### Residential Building window initialisation #####
def residentialBuildingWindow(rootWindow, screenWidth, screenHeight): 
    
    residentialBuildingWindow = tk.Toplevel(rootWindow)
    residentialBuildingWindow.title("CNPP Practical Guide - Residential Building")
    #residentialBuildingWindow.iconbitmap("Resources/Images/HydroGainLogo_NoText.ico")
    residentialBuildingWindow.iconbitmap("Resources/Images/CNPPLogo_Simple.ico")
    residentialBuildingWindow.geometry(str(int(screenWidth*1.2)) + "x" + str(int(screenHeight*1.2)))
    
    residentialBuildingWindow.rowconfigure(0, weight = 1)
    residentialBuildingWindow.rowconfigure(1, weight = 1)
    residentialBuildingWindow.rowconfigure(2, weight = 1)
    residentialBuildingWindow.rowconfigure(3, weight = 1)
    residentialBuildingWindow.rowconfigure(4, weight = 1)
    residentialBuildingWindow.rowconfigure(5, weight = 1)
    residentialBuildingWindow.rowconfigure(6, weight = 1)
    residentialBuildingWindow.rowconfigure(7, weight = 1)
    residentialBuildingWindow.rowconfigure(8, weight = 1)
    residentialBuildingWindow.rowconfigure(9, weight = 1)
    residentialBuildingWindow.rowconfigure(10, weight = 1)
    residentialBuildingWindow.rowconfigure(11, weight = 1)

    residentialBuildingWindow.columnconfigure(0, weight = 1)
    residentialBuildingWindow.columnconfigure(1, weight = 1)
    residentialBuildingWindow.columnconfigure(2, weight = 5)
    
    
    ##############################
    
    
    ### FUNCTIONS ###
    residentialBuildingObjects = []
    residentialBuildingObjectValue = {
        "buildingClassTxt" : "N/A",
        "flowRateTxt" : "N/A",
        "fireHydrantPointsNmbTxt" : "N/A",
        "fireHydrantPointsDistanceTxt" : "N/A",
        "fireHydrantPointsEntranceDistanceTxt" : "N/A",
        "minimalDurationTxt" : "N/A"}


    def createResidentialBuildingButton():
        name              = buildingNameEntryVar.get()
        buildingType      = buildingTypeTextVar.get()
        stageNmb          = stageNmbIntVar.get()
        height            = buildingHeightEntryVar.get()
        stairsDistance    = buildingStairsDistanceEntryVar.get()
        ladderTruckAccess = buildingLadderTruckAccessVar.get()
        
        building = rB.ResidentialBuilding(name, buildingType, stageNmb, height, stairsDistance, ladderTruckAccess)
        residentialBuildingObjects.append(building)
        
        buildingLabel = ttk.Label(summaryFrame, text = str(building), font = ("TkDefaultFont", 10), foreground = hydrogainBlue)
        buildingLabel.pack()
        summaryCanvas.config(scrollregion = summaryCanvas.bbox("all"))
        
        
    def clearResidentialBuildingButton():
        if len(residentialBuildingObjects) > 0:
            del residentialBuildingObjects[-1]
            
            labelChildren = summaryFrame.winfo_children()
            if len(labelChildren) != 0:
                lastWidget = labelChildren[-1]
                lastWidget.destroy()
            
        
    def calculationButton():
        if len(residentialBuildingObjects) > 0:
            i = residentialBuildingObjects[-1]
            buildingClassValue.config(text                     = i.buildingClass())
            flowRateValue.config(text                          = i.flowRateCalculation())
            fireHydrantPointsNmbValue.config(text              = i.fireHydrantPointsCalculation())
            fireHydrantPointsDistanceValue.config(text         = i.distanceFireHydrantPoints())
            fireHydrantPointsEntranceDistanceValue.config(text = i.distanceFireHydrantEntrance())
            minimalDurationValue.config(text                   = i.minimalDurationCalculation())
        else:
            residentialBuildingObjectValue["buildingClassTxt"]                     = "N/A"
            residentialBuildingObjectValue["flowRateTxt"]                          = "N/A"
            residentialBuildingObjectValue["fireHydrantPointsNmbTxt"]              = "N/A"
            residentialBuildingObjectValue["fireHydrantPointsDistanceTxt"]         = "N/A"
            residentialBuildingObjectValue["fireHydrantPointsEntranceDistanceTxt"] = "N/A"
            residentialBuildingObjectValue["minimalDurationTxt"]                   = "N/A"
        
                
    def generateLaTexFile():
        pass
    
        
    ##############################
        
    
    ### Row 0 ###
    residentialClassTitle = ttk.Label(residentialBuildingWindow, text = "Residential building", font = ("TkDefaultFont", 20, "bold"), foreground = hydrogainBlue)
    residentialClassTitle.grid(row = 0, column = 0, columnspan = 10)
    
    ### Row 1 ###
    buildingNameLabel = ttk.Label(residentialBuildingWindow, text = "Building name", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingNameLabel.grid(row = 1, column = 0)
    
    buildingNameEntryVar = tk.StringVar()
    buildingNameEntryVar.set("Residential building")
    buildingNameEntry    = ttk.Entry(residentialBuildingWindow,  textvariable = buildingNameEntryVar)
    buildingNameEntry.grid(row = 1, column = 1, sticky = "we")
    
    ### Row 2 ###
    buildingTypeLabel = ttk.Label(residentialBuildingWindow, text = "Building type", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingTypeLabel.grid(row = 2, column = 0)
    
    buildingTypeList     = ["individual", "collective"]
    buildingTypeTextVar  = tk.StringVar()
    buildingTypeTextVar.set("individual")
    buildingTypeCombobox = ttk.Combobox(residentialBuildingWindow, values = buildingTypeList, textvariable = buildingTypeTextVar)
    buildingTypeCombobox.grid(row = 2, column = 1, sticky = "we")
    
    ### Row 3 ###
    stageNmbLabel = ttk.Label(residentialBuildingWindow, text = "Number of stages [-]", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    stageNmbLabel.grid(row = 3, column = 0)
    
    stageNmbIntVar = tk.IntVar()
    stageNmbIntVar.set(1)
    stageNmbEntry  = ttk.Entry(residentialBuildingWindow, textvariable = stageNmbIntVar)
    stageNmbEntry.grid(row = 3, column = 1, sticky = "we")
    
    ### Row 4 ###
    buildingHeightLabel = ttk.Label(residentialBuildingWindow, text = "Building height [m]", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingHeightLabel.grid(row = 4, column = 0)
    
    buildingHeightEntryVar = tk.DoubleVar()
    buildingHeightEntryVar.set(10.0)
    buildingHeightEntry    = ttk.Entry(residentialBuildingWindow, textvariable = buildingHeightEntryVar)
    buildingHeightEntry.grid(row = 4, column = 1, sticky = "we")
    
    ### Row 5 ###
    buildingStairsDistanceLabel = ttk.Label(residentialBuildingWindow, text = "Stairs distance [m]", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingStairsDistanceLabel.grid(row = 5, column = 0)
    
    buildingStairsDistanceEntryVar = tk.DoubleVar()
    buildingStairsDistanceEntryVar.set(50.0)
    buildingStairsDistanceEntry    = ttk.Entry(residentialBuildingWindow, textvariable = buildingStairsDistanceEntryVar)
    buildingStairsDistanceEntry.grid(row = 5, column = 1, sticky = "we")
    
    ### Row 6 ###
    buildingLadderTruckAccessLabel = ttk.Label(residentialBuildingWindow, text = "Access to the stairs from the \"ladder truck\" way ?", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingLadderTruckAccessLabel.grid(row = 6, column = 0)
    
    frame = ttk.Frame(residentialBuildingWindow)
    frame.grid(row = 6, column = 1)
    
    buildingLadderTruckAccessVar = tk.BooleanVar()
    buildingLadderTruckAccessVar.set(True)
    buildingLadderTruckAccessRadioTrue  = ttk.Radiobutton(frame, text = "True", variable = buildingLadderTruckAccessVar, value = True)
    buildingLadderTruckAccessRadioFalse = ttk.Radiobutton(frame, text = "False", variable = buildingLadderTruckAccessVar, value = False)
            
    buildingLadderTruckAccessRadioTrue.grid(row = 0, column = 0, padx = 5)
    buildingLadderTruckAccessRadioFalse.grid(row = 0, column = 1, padx = 5)
    
    ### Row 7 ### 
    style = ttk.Style()
    style.configure("Green.TButton", font=("TkDefaultFont", 12, "bold"), foreground = hydrogainGreen)
    
    createBuildingButton = ttk.Button(residentialBuildingWindow, text = "CREATE BUILDING", style = "Green.TButton", command = createResidentialBuildingButton)
    createBuildingButton.grid(row = 7, column = 0, columnspan = 2, sticky = "nswe", padx = 30, pady = 5, ipady = 10)
    
    ### Row 8 ###
    style = ttk.Style()
    style.configure("Red.TButton", font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    
    calculateButton = ttk.Button(residentialBuildingWindow, text = "CALCULATE", style = "Red.TButton", command = calculationButton)
    calculateButton.grid(row = 8, column = 0, columnspan = 2, sticky = "nswe", padx = 30, pady = 5, ipady = 10)
    
    ### Row 9 ###
    style = ttk.Style()
    style.configure("HGBlue.TButton", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    
    createBuildingButton = ttk.Button(residentialBuildingWindow, text = "GENERATE LaTeX", style = "HGBlue.TButton", command = generateLaTexFile)
    createBuildingButton.grid(row = 9, column = 0, columnspan = 2, sticky = "nswe", padx = 30, pady = 5, ipady = 10)
   
    
   
    ##### RESULTS GUI #####
    calculationFrame = tk.Frame(residentialBuildingWindow)
    calculationFrame.grid(row = 7, column = 2, rowspan = 3, sticky = "we", padx = 10, pady = 10)
    
    calculationFrame.rowconfigure(0, weight = 1)
    calculationFrame.rowconfigure(1, weight = 1)
    calculationFrame.rowconfigure(2, weight = 1)
    calculationFrame.rowconfigure(3, weight = 1)
    calculationFrame.rowconfigure(4, weight = 1)
    calculationFrame.rowconfigure(5, weight = 1)
    calculationFrame.rowconfigure(6, weight = 1)
    
    calculationFrame.columnconfigure(0, weight = 1)
    calculationFrame.columnconfigure(1, weight = 1)
    
    
    resultsLabel = ttk.Label(calculationFrame, text = "Results", font = ("TkDefaultFont", 16, "bold"), foreground = hydrogainBlue)
    resultsLabel.grid(row = 0, column = 0, columnspan = 2, padx = 30)   
    
    buildingClassLabel = ttk.Label(calculationFrame, text = "Building class", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingClassLabel.grid(row = 1, column = 0, sticky = "w")
    buildingClassValue = ttk.Label(calculationFrame, text = residentialBuildingObjectValue["buildingClassTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    buildingClassValue.grid(row = 1, column = 1)
    
    flowRateLabel = ttk.Label(calculationFrame, text = "Flow-rate [m3.h-1]", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    flowRateLabel.grid(row = 2, column = 0, sticky = "w")
    flowRateValue = ttk.Label(calculationFrame, text = residentialBuildingObjectValue["flowRateTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    flowRateValue.grid(row = 2, column = 1)
    
    fireHydrantPointsNmbLabel = ttk.Label(calculationFrame, text = "Number of Fire Hydrant points", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    fireHydrantPointsNmbLabel.grid(row = 3, column = 0, sticky = "w")
    fireHydrantPointsNmbValue = ttk.Label(calculationFrame, text = residentialBuildingObjectValue["fireHydrantPointsNmbTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    fireHydrantPointsNmbValue.grid(row = 3, column = 1)
    
    fireHydrantPointsDistanceLabel = ttk.Label(calculationFrame, text = "Distance btw Fire Hydrant points", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    fireHydrantPointsDistanceLabel.grid(row = 4, column = 0, sticky = "w")
    fireHydrantPointsDistanceValue = ttk.Label(calculationFrame, text = residentialBuildingObjectValue["fireHydrantPointsDistanceTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    fireHydrantPointsDistanceValue.grid(row = 4, column = 1)
    
    fireHydrantPointsEntranceDistanceLabel = ttk.Label(calculationFrame, text = "Distance btw Fire Hydrant and the entrance", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    fireHydrantPointsEntranceDistanceLabel.grid(row = 5, column = 0, sticky = "w")
    fireHydrantPointsEntranceDistanceValue = ttk.Label(calculationFrame, text = residentialBuildingObjectValue["fireHydrantPointsEntranceDistanceTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    fireHydrantPointsEntranceDistanceValue.grid(row = 5, column = 1)
    
    minimalDurationLabel = ttk.Label(calculationFrame, text = "Minimum duration for the application of water", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    minimalDurationLabel.grid(row = 6, column = 0, sticky = "w")
    minimalDurationValue = ttk.Label(calculationFrame, text = residentialBuildingObjectValue["minimalDurationTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    minimalDurationValue.grid(row = 6, column = 1)
    
    
        
    ### SUMMARY ### 
    canvasFrame = ttk.Frame(residentialBuildingWindow)
    canvasFrame.grid(row = 1, column = 2, rowspan = 6, sticky = "nsew", padx = 10)
    canvasFrame.grid_rowconfigure(0, weight = 1)  
    canvasFrame.grid_columnconfigure(0, weight = 0) 
    canvasFrame.grid_columnconfigure(1, weight = 1)  

    
    summaryCanvas = tk.Canvas(canvasFrame)
    summaryCanvas.grid(row = 0, column = 1, sticky = "nsew")
    
    
    verticalScrollbar = ttk.Scrollbar(canvasFrame, orient = "vertical", command = summaryCanvas.yview)
    verticalScrollbar.grid(row = 0, column = 0, sticky = "ns")
    
    horizontalScrollbar = ttk.Scrollbar(canvasFrame, orient = "horizontal", command = summaryCanvas.xview)
    horizontalScrollbar.grid(row = 1, column = 1, sticky = "we")
    
    
    summaryCanvas.configure(yscrollcommand = verticalScrollbar.set, xscrollcommand = horizontalScrollbar.set)
    
    summaryFrame = ttk.Frame(summaryCanvas)
    summaryCanvas.create_window((0, 0), window = summaryFrame, anchor = "nw")
    
    summaryCanvas.config(scrollregion = summaryCanvas.bbox("all"))
    
 


    

    
    
    
    