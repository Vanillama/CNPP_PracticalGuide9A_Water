import tkinter as tk
from tkinter import ttk
import officeBuilding as oB


### Colours ###
hydrogainBlue  = "#263A91"
hydrogainGreen = "#A1CA18"



##### Office Building window initialisation #####
def officeBuildingWindow(rootWindow, screenWidth, screenHeight):
    
    officeBuildingWindow = tk.Toplevel(rootWindow)
    officeBuildingWindow.title("CNPP Practical Guide - Office Building")
    #officeBuildingWindow.iconbitmap("Resources/Images/HydroGainLogo_NoText.ico")
    officeBuildingWindow.iconbitmap("Resources/Images/CNPPLogo_Simple.ico")
    officeBuildingWindow.geometry(str(int(screenWidth*1.2)) + "x" + str(int(screenHeight*1.2)))
    
    officeBuildingWindow.rowconfigure(0, weight = 1)
    officeBuildingWindow.rowconfigure(1, weight = 1)
    officeBuildingWindow.rowconfigure(2, weight = 1)
    officeBuildingWindow.rowconfigure(3, weight = 1)
    officeBuildingWindow.rowconfigure(4, weight = 1)
    officeBuildingWindow.rowconfigure(5, weight = 1)
    officeBuildingWindow.rowconfigure(6, weight = 1)
    
    officeBuildingWindow.columnconfigure(0, weight = 1)
    officeBuildingWindow.columnconfigure(1, weight = 1)
    officeBuildingWindow.columnconfigure(2, weight = 5)
    
    
    ##############################
    
    
    ### FUNCTIONS ###
    officeBuildingObjects = []
    officeBuildingObjectValue = {
        "flowRateTxt"                          : "N/A",
        "fireHydrantPointsNmbTxt"              : "N/A",
        "fireHydrantPointsDistanceTxt"         : "N/A",
        "fireHydrantPointsEntranceDistanceTxt" : "N/A",
        "minimalDurationTxt"                   : "N/A"}
    
    
    def createOfficeBuildingButton():
        ### Create building
        name    = buildingNameEntryVar.get()
        height  = buildingHeightEntryVar.get()
        surface = buildingSurfaceEntryVar.get()
        
        building = oB.OfficeBuilding(name, height, surface)
        officeBuildingObjects.append(building)
        
        ### Calculate current building results
        calculationButton()
        
        ### Print created building information in the Canvas
        buildingLabel = ttk.Label(summaryFrame, text = str(building), font = ("TkDefaultFont", 10), foreground = hydrogainBlue)
        buildingLabel.pack()
        summaryCanvas.update_idletasks()
        summaryCanvas.config(scrollregion = summaryCanvas.bbox("all"))
        
        
    def clearOfficeBuildingButton():
        if len(officeBuildingObjects) > 0:
            del officeBuildingObjects[-1]
            
            labelChildren = summaryFrame.winfo_children()
            if len(labelChildren) != 0:
                lastWidget = labelChildren[-1]
                lastWidget.destroy()
                
                ### Calculate current building results
                calculationButton()
                summaryCanvas.update_idletasks()
                summaryCanvas.config(scrollregion = summaryCanvas.bbox("all"))
    
    
    def calculationButton():
        if len(officeBuildingObjects) > 0:
            i = officeBuildingObjects[-1]
            
            ### Updtate "officeBuildingObjectValue" dict
            officeBuildingObjectValue["flowRateTxt"]                          = i.flowRateCalculation()
            officeBuildingObjectValue["fireHydrantPointsNmbTxt"]              = i.fireHydrantPointsCalculation()
            officeBuildingObjectValue["fireHydrantPointsDistanceTxt"]         = i.distanceFireHydrantPoints()
            officeBuildingObjectValue["fireHydrantPointsEntranceDistanceTxt"] = i.distanceFireHydrantEntrance()
            officeBuildingObjectValue["minimalDurationTxt"]                   = i.minimalDurationCalculation()
            
            ### Update label values 
            flowRateValue.config(text                          = i.flowRateCalculation())
            fireHydrantPointsNmbValue.config(text              = i.fireHydrantPointsCalculation())
            fireHydrantPointsDistanceValue.config(text         = i.distanceFireHydrantPoints())
            fireHydrantPointsEntranceDistanceValue.config(text = i.distanceFireHydrantEntrance())
            minimalDurationValue.config(text                   = i.minimalDurationCalculation())
        else:
            flowRateValue.config(text                          = "N/A")
            fireHydrantPointsNmbValue.config(text              = "N/A")
            fireHydrantPointsDistanceValue.config(text         = "N/A")
            fireHydrantPointsEntranceDistanceValue.config(text = "N/A")
            minimalDurationValue.config(text                   = "N/A")
           
            
    def generateLaTexFile():
        pass   
    
    
    ##############################
    
    
    ### Row 0 ###
    officeClassTitle = ttk.Label(officeBuildingWindow, text = "Office building", font = ("TkDefaultFont", 20, "bold"), foreground = hydrogainBlue)
    officeClassTitle.grid(row = 0, column = 0, columnspan = 10)
    
    ### Row 1 ###
    buildingNameLabel = ttk.Label(officeBuildingWindow, text = "Building name", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingNameLabel.grid(row = 1, column = 0)
    
    buildingNameEntryVar = tk.StringVar()
    buildingNameEntryVar.set("Office building")
    buildingNameEntry    = ttk.Entry(officeBuildingWindow, textvariable = buildingNameEntryVar)
    buildingNameEntry.grid(row = 1, column = 1, sticky = "we")
    
    ### Row 2 ###
    buildingHeightLabelFrame = ttk.Frame(officeBuildingWindow)
    buildingHeightLabelFrame.grid(row = 2, column = 0)
    
    buildingHeightLabel = ttk.Label(buildingHeightLabelFrame, text = "Building height [m]", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingHeightLabel.grid(row = 0, column = 0)
    buildingHeightLegendLabel = ttk.Label(buildingHeightLabelFrame, text = "Height of the floor of the highest level relative to the ground", font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    buildingHeightLegendLabel.grid(row = 1, column = 0)
    
    buildingHeightEntryVar = tk.DoubleVar()
    buildingHeightEntryVar.set(10.0)
    buildingHeightEntry    = ttk.Entry(officeBuildingWindow, textvariable = buildingHeightEntryVar)
    buildingHeightEntry.grid(row = 2, column = 1, sticky = "we")
    
    ### Row 3 ###
    buildingSurfaceLabelFrame = ttk.Frame(officeBuildingWindow)
    buildingSurfaceLabelFrame.grid(row = 3, column = 0)
    
    buildingSurfaceLabel = ttk.Label(buildingSurfaceLabelFrame, text = "Building surface [m2]", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingSurfaceLabel.grid(row = 0, column = 0)
    buildingSurfaceLabel = ttk.Label(buildingSurfaceLabelFrame, text = "Developed area not intersected by fire barriers", font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    buildingSurfaceLabel.grid(row = 1, column = 0)
    
    buildingSurfaceEntryVar = tk.DoubleVar()
    buildingSurfaceEntryVar.set(100.0)
    buildingSurfaceEntry    = ttk.Entry(officeBuildingWindow, textvariable = buildingSurfaceEntryVar)
    buildingSurfaceEntry.grid(row = 3, column = 1, sticky ="we")
    
    ##### BUTTONS #####
    ### Row 4 ###   
    style = ttk.Style()
    style.configure("Green.TButton", font=("TkDefaultFont", 12, "bold"), foreground = hydrogainGreen)
    
    createBuildingButton = ttk.Button(officeBuildingWindow, text = "CREATE BUILDING + CALCULATE", style = "Green.TButton", command = createOfficeBuildingButton)
    createBuildingButton.grid(row = 4, column = 0, columnspan = 2, sticky = "nswe", padx = 30, pady = 5, ipady = 10)
  
    ### Row 5 ###
    style = ttk.Style()
    style.configure("Red.TButton", font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    
    clearButton = ttk.Button(officeBuildingWindow, text = "CLEAR", style = "Red.TButton", command = clearOfficeBuildingButton)
    clearButton.grid(row = 5, column = 0, columnspan = 2, sticky = "nswe", padx = 30, pady = 5, ipady = 10)
    
    ### Row 6 ###
    style = ttk.Style()
    style.configure("HGBlue.TButton", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    
    createLatexFileButton = ttk.Button(officeBuildingWindow, text = "GENERATE LaTeX", style = "HGBlue.TButton", command = generateLaTexFile)
    createLatexFileButton.grid(row = 6, column = 0, columnspan = 2, sticky = "nswe", padx = 30, pady = 5, ipady = 10)
    
    
    
    ##### RESULTS GUI #####
    calculationFrame = ttk.Frame(officeBuildingWindow)
    calculationFrame.grid(row = 4, column = 2, rowspan = 3, sticky = "we", padx = 10, pady = 10)
    
    calculationFrame.rowconfigure(0, weight = 1)
    calculationFrame.rowconfigure(1, weight = 1)
    calculationFrame.rowconfigure(2, weight = 1)
    calculationFrame.rowconfigure(3, weight = 1)
    calculationFrame.rowconfigure(4, weight = 1)
    calculationFrame.rowconfigure(5, weight = 1)
    calculationFrame.rowconfigure(6, weight = 1)
    calculationFrame.rowconfigure(7, weight = 1)
    calculationFrame.rowconfigure(8, weight = 1)
    calculationFrame.rowconfigure(9, weight = 1)
    calculationFrame.rowconfigure(10, weight = 1)
    
    calculationFrame.columnconfigure(0, weight = 1)
    calculationFrame.columnconfigure(1, weight = 1)
    
    
    resultsLabel = ttk.Label(calculationFrame, text = "Current Building Results", font = ("TkDefaultFont", 16, "bold"), foreground = hydrogainBlue)
    resultsLabel.grid(row = 0, column = 0, columnspan = 2, padx = 30)   
    
    flowRateLabel = ttk.Label(calculationFrame, text = "Flow-rate [m3.h-1]", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    flowRateLabel.grid(row = 1, column = 0, sticky = "w")
    flowRateValue = ttk.Label(calculationFrame, text = officeBuildingObjectValue["flowRateTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    flowRateValue.grid(row = 2, column = 0, sticky = "w")
    
    fireHydrantPointsNmbLabel = ttk.Label(calculationFrame, text = "Number of Fire Hydrant points", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    fireHydrantPointsNmbLabel.grid(row = 3, column = 0, sticky = "w")
    fireHydrantPointsNmbValue = ttk.Label(calculationFrame, text = officeBuildingObjectValue["fireHydrantPointsNmbTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    fireHydrantPointsNmbValue.grid(row = 4, column = 0, sticky = "w")
    
    fireHydrantPointsDistanceLabel = ttk.Label(calculationFrame, text = "Distance btw Fire Hydrant points", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    fireHydrantPointsDistanceLabel.grid(row = 5, column = 0, sticky = "w")
    fireHydrantPointsDistanceValue = ttk.Label(calculationFrame, text = officeBuildingObjectValue["fireHydrantPointsDistanceTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    fireHydrantPointsDistanceValue.grid(row = 6, column = 0, sticky = "w")
    
    fireHydrantPointsEntranceDistanceLabel = ttk.Label(calculationFrame, text = "Distance btw Fire Hydrant and the entrance", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    fireHydrantPointsEntranceDistanceLabel.grid(row = 7, column = 0, sticky = "w")
    fireHydrantPointsEntranceDistanceValue = ttk.Label(calculationFrame, text = officeBuildingObjectValue["fireHydrantPointsEntranceDistanceTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    fireHydrantPointsEntranceDistanceValue.grid(row = 8, column = 0, sticky = "w")
    
    minimalDurationLabel = ttk.Label(calculationFrame, text = "Minimum duration for the application of water", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    minimalDurationLabel.grid(row = 9, column = 0, sticky = "w")
    minimalDurationValue = ttk.Label(calculationFrame, text = officeBuildingObjectValue["minimalDurationTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    minimalDurationValue.grid(row = 10, column = 0, sticky = "w")
   
    

    ### SUMMARY ###
    canvasFrame = ttk.Frame(officeBuildingWindow)
    canvasFrame.grid(row = 1, column = 2, rowspan = 3, sticky = "nswe", padx = 10)
    canvasFrame.grid_rowconfigure(0, weight = 1)  
    canvasFrame.grid_columnconfigure(0, weight = 0) 
    canvasFrame.grid_columnconfigure(1, weight = 1)  
    
    
    summaryCanvas = tk.Canvas(canvasFrame)
    summaryCanvas.grid(row = 0, column = 1, sticky = "nswe")
    
    
    verticalScrollbar = ttk.Scrollbar(canvasFrame, orient = "vertical", command = summaryCanvas.yview)
    verticalScrollbar.grid(row = 0, column = 0, sticky = "ns")
    
    horizontalScrollbar = ttk.Scrollbar(canvasFrame, orient = "horizontal", command = summaryCanvas.xview)
    horizontalScrollbar.grid(row = 1, column = 1, sticky = "we")
    
    
    summaryCanvas.configure(yscrollcommand = verticalScrollbar.set, xscrollcommand = horizontalScrollbar.set)
    
    summaryFrame = ttk.Frame(summaryCanvas)
    summaryCanvas.create_window((0, 0), window = summaryFrame, anchor = "nw")
    
    summaryCanvas.config(scrollregion = summaryCanvas.bbox("all"))      
        
        
        
        
        
        
        
        
    
    




















