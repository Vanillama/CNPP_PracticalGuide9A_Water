import tkinter as tk
from tkinter import ttk
import erpBuilding as erpB
import guiD9AGuide as d9a


### Colours ###
hydrogainBlue  = "#263A91"
hydrogainGreen = "#A1CA18"



##### ERP Building window initialisation #####
def erpBuildingWindow(rootWindow, screenWidth, screenHeight):
    
    erpBuildingWindow = tk.Toplevel(rootWindow)
    erpBuildingWindow.title("CNPP D9 Practical Guide - ERP Building")
    #erpBuildingWindow.iconbitmap("Resources/Images/HydroGainLogo_NoText.ico")
    erpBuildingWindow.iconbitmap("Resources/Images/CNPPLogo_Simple.ico")
    erpBuildingWindow.geometry(str(int(screenWidth*1.2)) + "x" + str(int(screenHeight*1.2)))
    
    erpBuildingWindow.rowconfigure(0, weight = 1)
    erpBuildingWindow.rowconfigure(1, weight = 1)
    erpBuildingWindow.rowconfigure(2, weight = 1)
    erpBuildingWindow.rowconfigure(3, weight = 1)
    erpBuildingWindow.rowconfigure(4, weight = 1)
    erpBuildingWindow.rowconfigure(5, weight = 1)
    erpBuildingWindow.rowconfigure(6, weight = 1)
    erpBuildingWindow.rowconfigure(7, weight = 1)
    erpBuildingWindow.rowconfigure(8, weight = 1)
    
    erpBuildingWindow.columnconfigure(0, weight = 1)
    erpBuildingWindow.columnconfigure(1, weight = 1)
    erpBuildingWindow.columnconfigure(2, weight = 5)
    
    
    ##############################
    
    
    ### FUNCTIONS ###
    erpBuildingObjects = []
    erpBuildingObjectValue = {
        "flowRateTxt"                          : "N/A",
        "fireHydrantPointsNmbTxt"              : "N/A",
        "fireHydrantPointsDistanceTxt"         : "N/A",
        "fireHydrantPointsEntranceDistanceTxt" : "N/A",
        "minimalDurationTxt"                   : "N/A"}
    
    
    def createERPBuildingButton():
        ### Create building
        name           = buildingNameEntryVar.get()
        buildingClass  = buildingClassTextVar.get()
        surface        = buildingSurfaceEntryVar.get()
        
        building = erpB.ErpBuilding(name, buildingClass, surface)
        erpBuildingObjects.append(building)
        
        ### Calculate current building results
        calculationButton()
        
        ### Print created building information in the Canvas
        summaryText = (str(building) + "\n"
                       "The building's name is : " + name + "\n"
                       "The calculated flowrate is [m3.h-1]: " + str(erpBuildingObjectValue["flowRateTxt"]))
        d9a.allBuildingsText.append(summaryText)
        
        buildingLabel = ttk.Label(summaryFrame, text = summaryText, font = ("TkDefaultFont", 10), foreground = hydrogainBlue)
        buildingLabel.pack()
        summaryCanvas.update_idletasks()
        summaryCanvas.config(scrollregion = summaryCanvas.bbox("all"))
    
    
    def clearERPBuildingButton():
        if len(erpBuildingObjects) > 0:
            del erpBuildingObjects[-1]
            del d9a.allBuildingsText[-1]
            
            labelChildren = summaryFrame.winfo_children()
            if len(labelChildren) != 0:
                lastWidget = labelChildren[-1]
                lastWidget.destroy()
                
                ### Calculate current building results
                calculationButton()
                summaryCanvas.update_idletasks()
                summaryCanvas.config(scrollregion = summaryCanvas.bbox("all"))
        
    
    def calculationButton():
        if len(erpBuildingObjects) > 0:
            i = erpBuildingObjects[-1]
            
            ### Updtate "residentialBuildingObjectValue" dict
            erpBuildingObjectValue["flowRateTxt"]                          = i.flowRateCalculation()
            erpBuildingObjectValue["fireHydrantPointsNmbTxt"]              = i.fireHydrantPointsCalculation()
            erpBuildingObjectValue["fireHydrantPointsDistanceTxt"]         = i.distanceFireHydrantPoints()
            erpBuildingObjectValue["fireHydrantPointsEntranceDistanceTxt"] = i.distanceFireHydrantEntrance()
            erpBuildingObjectValue["minimalDurationTxt"]                   = i.minimalDurationCalculation()
            
            ### Update label values    
            # flowRateValue.config(text                          = i.flowRateCalculation())
            # fireHydrantPointsNmbValue.config(text              = i.fireHydrantPointsCalculation())
            # fireHydrantPointsDistanceValue.config(text         = i.distanceFireHydrantPoints())
            # fireHydrantPointsEntranceDistanceValue.config(text = i.distanceFireHydrantEntrance())
            # minimalDurationValue.config(text                   = i.minimalDurationCalculation())
            flowRateValue.config(text                          = erpBuildingObjectValue["flowRateTxt"])
            fireHydrantPointsNmbValue.config(text              = erpBuildingObjectValue["fireHydrantPointsNmbTxt"])
            fireHydrantPointsDistanceValue.config(text         = erpBuildingObjectValue["fireHydrantPointsDistanceTxt"])
            fireHydrantPointsEntranceDistanceValue.config(text = erpBuildingObjectValue["fireHydrantPointsEntranceDistanceTxt"])
            minimalDurationValue.config(text                   = erpBuildingObjectValue["minimalDurationTxt"])
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
    erpClassTitle = ttk.Label(erpBuildingWindow, text = "ERP building", font = ("TkDefaultFont", 20, "bold"), foreground = hydrogainBlue)
    erpClassTitle.grid(row = 0, column = 0, columnspan = 10)
    
    ### Row 1 ###   
    buildingNameLabel = ttk.Label(erpBuildingWindow, text = "Building name", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingNameLabel.grid(row = 1, column = 0)
    
    buildingNameEntryVar = tk.StringVar()
    buildingNameEntryVar.set("ERP building")
    buildingNameEntry    = ttk.Entry(erpBuildingWindow,  textvariable = buildingNameEntryVar)
    buildingNameEntry.grid(row = 1, column = 1, sticky = "we")
    
    ### Row 2 ###  
    buildingClassLabelFrame = ttk.Frame(erpBuildingWindow)
    buildingClassLabelFrame.grid(row = 2, column = 0)
    
    buildingClassLabel = ttk.Label(buildingClassLabelFrame, text = "Building class", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingClassLabel.grid(row = 0, column = 0)
    
    buildingClassLegendFrame = ttk.Frame(buildingClassLabelFrame)
    buildingClassLegendFrame.grid(row = 1, column = 0, sticky = "nswe", padx = 50, pady = 5)
    
    textClass1 = """Restaurants / Meeting rooms - Performance halls (without decor or fireworks) / 
                Hotels / Education / Indoor sports facilities / Health care facilities / 
                Worship facilities / Offices..."""
    buildingClass1Legend = ttk.Label(buildingClassLegendFrame, text = "Class 1 : " + textClass1, font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    buildingClass1Legend.grid(row = 0, column = 0, sticky = "we")
    
    textClass2 = """Meeting rooms - Performance halls (with decor or fireworks) / Museums /
                Dance and games rooms..."""
    buildingClass2Legend = ttk.Label(buildingClassLegendFrame, text = "Class 2 : " + textClass2, font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    buildingClass2Legend.grid(row = 1, column = 0, sticky = "we")
    
    textClass3 = "Stores / Libraries - Documentation rooms / Exhibitions..."
    buildingClass3Legend = ttk.Label(buildingClassLegendFrame, text = "Class 3 : " + textClass3, font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    buildingClass3Legend.grid(row = 2, column = 0, sticky = "we")
    
    textClass4 = "Protected by an automatic water extinguishing system (all classes)"
    buildingClassProtectLegend = ttk.Label(buildingClassLegendFrame, text = "Protected : " + textClass4, font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    buildingClassProtectLegend.grid(row = 3, column = 0, sticky = "we")
    
    
    buildingClassList    = ["Class 1", "Class 2", "Class 3", "Protected"]
    buildingClassTextVar = tk.StringVar()
    buildingClassTextVar.set("Class 1")
    buildingClassCombobox = ttk.Combobox(erpBuildingWindow, values = buildingClassList, textvariable = buildingClassTextVar)
    buildingClassCombobox.grid(row = 2, column = 1, sticky = "nwe", pady = 30)
    
    ### Row 3 ###
    buildingSurfaceLabelFrame = ttk.Frame(erpBuildingWindow)
    buildingSurfaceLabelFrame.grid(row = 3, column = 0)
    
    buildingSurfaceLabel = ttk.Label(buildingSurfaceLabelFrame, text = "Building surface [m2]", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingSurfaceLabel.grid(row = 0, column = 0)
    buildingSurfaceLabel = ttk.Label(buildingSurfaceLabelFrame, text = "Developed area not intersected by fire barriers", font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    buildingSurfaceLabel.grid(row = 1, column = 0)
    
    buildingSurfaceEntryVar = tk.DoubleVar()
    buildingSurfaceEntryVar.set(100.0)
    buildingSurfaceEntry    = ttk.Entry(erpBuildingWindow,  textvariable = buildingSurfaceEntryVar)
    buildingSurfaceEntry.grid(row = 3, column = 1, sticky = "we")
    
    ##### BUTTONS #####
    ### Row 4 ###   
    style = ttk.Style()
    style.configure("Green.TButton", font=("TkDefaultFont", 12, "bold"), foreground = hydrogainGreen)
    
    createBuildingButton = ttk.Button(erpBuildingWindow, text = "CREATE BUILDING + CALCULATE", style = "Green.TButton", command = createERPBuildingButton)
    createBuildingButton.grid(row = 5, column = 0, columnspan = 2, sticky = "nswe", padx = 30, pady = 5, ipady = 10)
  
    ### Row 5 ###
    style = ttk.Style()
    style.configure("Red.TButton", font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    
    clearButton = ttk.Button(erpBuildingWindow, text = "CLEAR", style = "Red.TButton", command = clearERPBuildingButton)
    clearButton.grid(row = 7, column = 0, columnspan = 2, sticky = "nswe", padx = 30, pady = 5, ipady = 10)
    
    ### Row 6 ###
    # style = ttk.Style()
    # style.configure("HGBlue.TButton", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    
    # createLatexFileButton = ttk.Button(erpBuildingWindow, text = "GENERATE LaTeX", style = "HGBlue.TButton", command = generateLaTexFile)
    # createLatexFileButton.grid(row = 6, column = 0, columnspan = 2, sticky = "nswe", padx = 30, pady = 5, ipady = 10)
       
    
    
    ##### RESULTS GUI #####
    calculationFrame = ttk.Frame(erpBuildingWindow)
    calculationFrame.grid(row = 4, column = 2, rowspan = 5, sticky = "we", padx = 10, pady = 10)
    
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
    flowRateValue = ttk.Label(calculationFrame, text = erpBuildingObjectValue["flowRateTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    flowRateValue.grid(row = 2, column = 0, sticky = "w")
    
    fireHydrantPointsNmbLabel = ttk.Label(calculationFrame, text = "Number of Fire Hydrant points", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    fireHydrantPointsNmbLabel.grid(row = 3, column = 0, sticky = "w")
    fireHydrantPointsNmbValue = ttk.Label(calculationFrame, text = erpBuildingObjectValue["fireHydrantPointsNmbTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    fireHydrantPointsNmbValue.grid(row = 4, column = 0, sticky = "w")
    
    fireHydrantPointsDistanceLabel = ttk.Label(calculationFrame, text = "Distance btw Fire Hydrant points", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    fireHydrantPointsDistanceLabel.grid(row = 5, column = 0, sticky = "w")
    fireHydrantPointsDistanceValue = ttk.Label(calculationFrame, text = erpBuildingObjectValue["fireHydrantPointsDistanceTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    fireHydrantPointsDistanceValue.grid(row = 6, column = 0, sticky = "w")
    
    fireHydrantPointsEntranceDistanceLabel = ttk.Label(calculationFrame, text = "Distance btw Fire Hydrant and the entrance", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    fireHydrantPointsEntranceDistanceLabel.grid(row = 7, column = 0, sticky = "w")
    fireHydrantPointsEntranceDistanceValue = ttk.Label(calculationFrame, text = erpBuildingObjectValue["fireHydrantPointsEntranceDistanceTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    fireHydrantPointsEntranceDistanceValue.grid(row = 8, column = 0, sticky = "w")
    
    minimalDurationLabel = ttk.Label(calculationFrame, text = "Minimum duration for the application of water", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    minimalDurationLabel.grid(row = 9, column = 0, sticky = "w")
    minimalDurationValue = ttk.Label(calculationFrame, text = erpBuildingObjectValue["minimalDurationTxt"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    minimalDurationValue.grid(row = 10, column = 0, sticky = "w")
       
    
    
    ### SUMMARY ###
    canvasFrame = ttk.Frame(erpBuildingWindow)
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    