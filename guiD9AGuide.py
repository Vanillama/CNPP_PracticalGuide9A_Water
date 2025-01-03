import tkinter as tk
from tkinter import ttk


### Colours ###
hydrogainBlue  = "#263A91"
hydrogainGreen = "#A1CA18"


allBuildingsText = [] # List containing all building texts created using D9 Codes

##### Retention volume (D9A) window initialisation #####
def d9aCalculationWindow(rootWindow, screenWidth, screenHeight):
    
    d9aCalculationWindow = tk.Toplevel(rootWindow)
    d9aCalculationWindow.title("CNPP D9A Practical Guide - Water Retention Volume")
    #d9aCalculationWindow.iconbitmap("Resources/Images/HydroGainLogo_NoText.ico")
    d9aCalculationWindow.iconbitmap("Resources/Images/CNPPLogo_Simple.ico")
    d9aCalculationWindow.geometry(str(int(screenWidth*1.2)) + "x" + str(int(screenHeight*1.2)))
    
    d9aCalculationWindow.rowconfigure(0, weight = 1)
    d9aCalculationWindow.rowconfigure(1, weight = 1)
    d9aCalculationWindow.rowconfigure(2, weight = 1)
    d9aCalculationWindow.rowconfigure(3, weight = 1)
    d9aCalculationWindow.rowconfigure(4, weight = 1)
    d9aCalculationWindow.rowconfigure(5, weight = 1)
    d9aCalculationWindow.rowconfigure(6, weight = 1)
    d9aCalculationWindow.rowconfigure(7, weight = 1)
    d9aCalculationWindow.rowconfigure(8, weight = 1)
    d9aCalculationWindow.rowconfigure(9, weight = 1)
    d9aCalculationWindow.rowconfigure(10, weight = 1)
    d9aCalculationWindow.rowconfigure(11, weight = 1)
    d9aCalculationWindow.rowconfigure(12, weight = 1)
    d9aCalculationWindow.rowconfigure(13, weight = 1)

    d9aCalculationWindow.columnconfigure(0, weight = 1)
    d9aCalculationWindow.columnconfigure(1, weight = 1)
    d9aCalculationWindow.columnconfigure(2, weight = 5)
    
    
    ##############################
    
    
    ### FUNCTIONS ###
    def updateCalculateVolume():
        ### Collect values
        extWaterFlowRate   = d9RequirementEntryVar.get()
        sprinklerVolume    = sprinklerEntryVar.get()
        waterCurtainVolume = waterCurtainEntryVar.get()
        foamVolume         = foamEntryVar.get()
        mistVolume         = waterMistEntryVar.get()
        standPipeVolume    = standpipeEntryVar.get()
        surface            = surfaceEntryVar.get()
        totalStorageVolume = storageEntryVar.get()
        
        ### Calculation
        extWaterVolume    = extWaterFlowRate * 2
        weatherVolume     = surface * 0.01
        flamStorageVolume = totalStorageVolume * 0.2
        
        finalVolume       = extWaterVolume + sprinklerVolume + waterCurtainVolume + foamVolume + mistVolume + standPipeVolume + weatherVolume + flamStorageVolume
        
        ### Update label values           
        d9RequirementValLabel.config(text = extWaterVolume)
        weatherLegendLabel.config(text    = weatherVolume)
        volumeLegendLabel.config(text     = flamStorageVolume)
        d9aGuideResult.config(text        = finalVolume)


    def clearBuildingButton():
        if len(allBuildingsText) > 0:
            del allBuildingsText[-1]
            
            labelChildren = summaryFrame.winfo_children()
            if len(labelChildren) != 0:
                lastWidget = labelChildren[-1]
                lastWidget.destroy()
                
                summaryCanvas.update_idletasks()
                summaryCanvas.config(scrollregion = summaryCanvas.bbox("all"))
            
    
    ### Row 0 ###
    d9aGuideTitle = ttk.Label(d9aCalculationWindow, text = "Water Retention Volume Calculation", font = ("TkDefaultFont", 20, "bold"), foreground = hydrogainBlue)
    d9aGuideTitle.grid(row = 0, column = 0, columnspan = 10)
    
    
    ### Row 1 / 2 ###  
    d9RequirementLabel = ttk.Label(d9aCalculationWindow, text = "External water flow-rate", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    d9RequirementLabel.grid(row = 1, column = 0)
    
    d9RequirementEntryVar = tk.DoubleVar()
    d9RequirementEntryVar.set(0.0)
    d9RequirementEntry    = ttk.Entry(d9aCalculationWindow,  textvariable = d9RequirementEntryVar)
    d9RequirementEntry.grid(row = 1, column = 1, sticky = "we")
    
    
    d9RequirementLegendLabel = ttk.Label(d9aCalculationWindow, text = "D9 Guide calculation (2 hours) [m3]", font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    d9RequirementLegendLabel.grid(row = 2, column = 0)
    d9RequirementValLabel = ttk.Label(d9aCalculationWindow, text = "N/A", font = ("TkDefaultFont", 8, "bold"), foreground = "red")
    d9RequirementValLabel.grid(row = 2, column = 1) 
    
    
    ### Row 3 ###
    srinklerFrame = ttk.Frame(d9aCalculationWindow)
    srinklerFrame.grid(row = 3, column = 0)
    
    
    textSprinkler = """Total reserve volume of the main source OR 
Requirements * Maximum theoretical operating time [m3]"""
    sprinklerLabel = ttk.Label(srinklerFrame, text = "Internal firefighting - Sprinkler", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    sprinklerLabel.grid(row = 0, column = 0)
    sprinklerLegendLabel = ttk.Label(srinklerFrame, text = textSprinkler, font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    sprinklerLegendLabel.grid(row = 1, column = 0)
    
    sprinklerEntryVar = tk.DoubleVar()
    sprinklerEntryVar.set(0.0)
    sprinklerEntry    = ttk.Entry(d9aCalculationWindow,  textvariable = sprinklerEntryVar)
    sprinklerEntry.grid(row = 3, column = 1, sticky = "we")
    
    
    ### Row 4 ###
    waterCurtainFrame = ttk.Frame(d9aCalculationWindow)
    waterCurtainFrame.grid(row = 4, column = 0)
    
    
    textWaterCurtain = """Requirements *90 min [m3]"""
    waterCurtainLabel = ttk.Label(waterCurtainFrame, text = "Internal firefighting - Water curtain", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    waterCurtainLabel.grid(row = 0, column = 0)
    waterCurtainLegendLabel = ttk.Label(waterCurtainFrame, text = textWaterCurtain, font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    waterCurtainLegendLabel.grid(row = 1, column = 0)
    
    waterCurtainEntryVar = tk.DoubleVar()
    waterCurtainEntryVar.set(0.0)
    waterCurtainEntry    = ttk.Entry(d9aCalculationWindow,  textvariable = waterCurtainEntryVar)
    waterCurtainEntry.grid(row = 4, column = 1, sticky = "we")
    
    
    ### Row 5 ###
    foamFrame = ttk.Frame(d9aCalculationWindow)
    foamFrame.grid(row = 5, column = 0)
    
    
    textFoam = """Foam solution flow rate * Flooding time (generally 15-25 minutes) [m3]"""
    foamLabel = ttk.Label(foamFrame, text = "Internal firefighting - HF and MF foam", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    foamLabel.grid(row = 0, column = 0)
    foamLegendLabel = ttk.Label(foamFrame, text = textWaterCurtain, font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    foamLegendLabel.grid(row = 1, column = 0)
    
    foamEntryVar = tk.DoubleVar()
    foamEntryVar.set(0.0)
    foamEntry    = ttk.Entry(d9aCalculationWindow,  textvariable = foamEntryVar)
    foamEntry.grid(row = 5, column = 1, sticky = "we")
    
    
    ### Row 6 ###
    waterMistFrame = ttk.Frame(d9aCalculationWindow)
    waterMistFrame.grid(row = 6, column = 0)
    
    
    textWaterMist = """Flow rate * Required operating time [m3]"""
    waterMistLabel = ttk.Label(waterMistFrame, text = "Internal firefighting - Water mist / Others", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    waterMistLabel.grid(row = 0, column = 0)
    waterMistLegendLabel = ttk.Label(waterMistFrame, text = textWaterMist, font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    waterMistLegendLabel.grid(row = 1, column = 0)
    
    waterMistEntryVar = tk.DoubleVar()
    waterMistEntryVar.set(0.0)
    waterMistEntry    = ttk.Entry(d9aCalculationWindow,  textvariable = waterMistEntryVar)
    waterMistEntry.grid(row = 6, column = 1, sticky = "we")
    
    
    ### Row 7 ###
    standpipeFrame = ttk.Frame(d9aCalculationWindow)
    standpipeFrame.grid(row = 7, column = 0)
    
    
    textStandpipe = """Flow rate * Required operating time [m3]"""
    standpipeLabel = ttk.Label(standpipeFrame, text = "Internal firefighting - Standpipe", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    standpipeLabel.grid(row = 0, column = 0)
    standpipeLegendLabel = ttk.Label(standpipeFrame, text = textWaterMist, font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    standpipeLegendLabel.grid(row = 1, column = 0)
    
    standpipeEntryVar = tk.DoubleVar()
    standpipeEntryVar.set(0.0)
    standpipeEntry    = ttk.Entry(d9aCalculationWindow,  textvariable = standpipeEntryVar)
    standpipeEntry.grid(row = 7, column = 1, sticky = "we")
    
    
    ### Row 8 / 9 ###
    weatherFrame1 = ttk.Frame(d9aCalculationWindow)
    weatherFrame1.grid(row = 8, column = 0)
    
    weatherFrame2 = ttk.Frame(d9aCalculationWindow)
    weatherFrame2.grid(row = 9, column = 0)
     
    
    textSurface = """Impermeabilized surface [m2]"""
    surfaceLabel = ttk.Label(weatherFrame1, text = "Surface", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    surfaceLabel.grid(row = 0, column = 0)
    surfaceLegendLabel = ttk.Label(weatherFrame1, text = textSurface, font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    surfaceLegendLabel.grid(row = 1, column = 0)
    
    surfaceEntryVar = tk.DoubleVar()
    surfaceEntryVar.set(0.0)
    surfaceEntry    = ttk.Entry(d9aCalculationWindow,  textvariable = surfaceEntryVar)
    surfaceEntry.grid(row = 8, column = 1, sticky = "we")
    
    
    textWeather = """Water volumes related to weather conditions
    0,01 m3/m2 * Drainage surface [m3]"""
    weatherLabel = ttk.Label(weatherFrame2, text = textWeather, font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    weatherLabel.grid(row = 0, column = 0)

    weatherLegendLabel = ttk.Label(d9aCalculationWindow, text = "N/A", font = ("TkDefaultFont", 8, "bold"), foreground = "red")
    weatherLegendLabel.grid(row = 9, column = 1)
    
    
    ### Row 10 / 11 ###
    liquidStorageFrame1 = ttk.Frame(d9aCalculationWindow)
    liquidStorageFrame1.grid(row = 10, column = 0)
    
    liquidStorageFrame2 = ttk.Frame(d9aCalculationWindow)
    liquidStorageFrame2.grid(row = 11, column = 0)
     
    
    textStorage = """Total flammable liquid storage [m3]"""
    storageLabel = ttk.Label(liquidStorageFrame1, text = "Storage volume", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    storageLabel.grid(row = 0, column = 0)
    storageLegendLabel = ttk.Label(liquidStorageFrame1, text = textStorage, font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    storageLegendLabel.grid(row = 1, column = 0)
    
    storageEntryVar = tk.DoubleVar()
    storageEntryVar.set(0.0)
    storageEntry    = ttk.Entry(d9aCalculationWindow,  textvariable = storageEntryVar)
    storageEntry.grid(row = 10, column = 1, sticky = "we")
    
    
    textVolume = """20% of the volume contained in the storage [m3]"""
    volumeLabel = ttk.Label(liquidStorageFrame2, text = textVolume, font = ("TkDefaultFont", 8, "italic"), foreground = hydrogainBlue)
    volumeLabel.grid(row = 0, column = 0)

    volumeLegendLabel = ttk.Label(d9aCalculationWindow, text = "N/A", font = ("TkDefaultFont", 8, "bold"), foreground = "red")
    volumeLegendLabel.grid(row = 11, column = 1)
    
    
    ##### BUTTONS #####
    ### Row 12 ### 
    style = ttk.Style()
    style.configure("Green.TButton", font=("TkDefaultFont", 12, "bold"), foreground = hydrogainGreen)
    
    createBuildingButton = ttk.Button(d9aCalculationWindow, text = "UPDATE", style = "Green.TButton", command = updateCalculateVolume)
    createBuildingButton.grid(row = 12, column = 0, columnspan = 2, sticky = "nswe", padx = 30, pady = 5, ipady = 10)
    
    ### Row 13 ###
    style = ttk.Style()
    style.configure("Red.TButton", font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    
    clearButton = ttk.Button(d9aCalculationWindow, text = "CLEAR", style = "Red.TButton", command = clearBuildingButton)
    clearButton.grid(row = 13, column = 0, columnspan = 2, sticky = "nswe", padx = 30, pady = 5, ipady = 10)
    
    
    ##### FINAL RESULT #####
    finalResultFrame = ttk.Frame(d9aCalculationWindow)
    finalResultFrame.grid(row = 12, column = 2, rowspan = 2)
    
    d9aGuideResultTitle = ttk.Label(finalResultFrame, text = "RESULT [m3.h-1]", font = ("TkDefaultFont", 20, "bold"), foreground = hydrogainBlue)
    d9aGuideResultTitle.grid(row = 0, column = 0)
    
    d9aGuideResult = ttk.Label(finalResultFrame, text = "N/A", font = ("TkDefaultFont", 20, "bold"), foreground = "red")
    d9aGuideResult.grid(row = 1, column = 0)
    

    
    ### SUMMARY ### 
    canvasFrame = ttk.Frame(d9aCalculationWindow)
    canvasFrame.grid(row = 1, column = 2, rowspan = 11, sticky = "nsew", padx = 10)
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
    
    
    
    ### INITIALISATION ###
    if len(allBuildingsText) > 0:
        for i in allBuildingsText:
            buildingLabel = ttk.Label(summaryFrame, text = i, font = ("TkDefaultFont", 10), foreground = hydrogainBlue)
            buildingLabel.pack()
            summaryCanvas.update_idletasks()
            summaryCanvas.config(scrollregion = summaryCanvas.bbox("all"))
            