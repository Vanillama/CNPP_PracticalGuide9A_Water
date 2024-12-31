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
    industrialBuildingWindow.rowconfigure(10, weight = 1)
    
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
        "currentBuildingFlowRate" : 0.0,
        "finalFlowRate" : 0.0,
        "riskCategoryCoef" : 0.0,
        "autoWaterExtinctCoef" : 0.0}
    
    def createIndustrialBuildingButton():
        name                       = buildingNameEntryVar.get()
        height                     = buildingHeightEntryVar.get()
        surface                    = buildingSurfaceEntryVar.get()
        buildingFireResistanceCoef = buildingFireResistanceCoefTextVar.get()
        hazardousMaterialCoef      = hazardousMaterialVar.get()
        internalInterventionCoef   = buildingInterventionTypeCoefTextVar.get()
        riskCategoryCoef           = buildingRiskCatTextVar.get()
        
        building = indB.IndustrialBuilding(name, height, surface, buildingFireResistanceCoef, hazardousMaterialCoef, internalInterventionCoef, riskCategoryCoef)
        industrialBuildingObjects.append(building)
        
        buildingLabel = ttk.Label(summaryFrame, text = str(building), font = ("TkDefaultFont", 10), foreground = hydrogainBlue)
        buildingLabel.pack()
        summaryCanvas.config(scrollregion = summaryCanvas.bbox("all"))
    
    
    
    def clearIndustrialBuildingButton():
        if len(industrialBuildingObjects) > 0:
            del industrialBuildingObjects[-1]
            
            labelChildren = summaryFrame.winfo_children()
            if len(labelChildren) != 0:
                lastWidget = labelChildren[-1]
                lastWidget.destroy()
    
    
    def calculationButton():
        pass
    
    
    def calculationButtonFinal():
        pass
    
    
    def generateLaTexFile():
        pass  

    
    ##############################
    
    
    ### Row 0 ###
    industrialClassTitle = ttk.Label(industrialBuildingWindow, text = "Industrial building", font = ("TkDefaultFont", 20, "bold"), foreground = hydrogainBlue)
    industrialClassTitle.grid(row = 0, column = 0, columnspan = 10)
    
    ### Row 1 ###
    buildingNameLabel = ttk.Label(industrialBuildingWindow, text = "Building name", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingNameLabel.grid(row = 1, column = 0)
    
    buildingNameEntryVar = tk.StringVar()
    buildingNameEntryVar.set("Industrial building")
    buildingNameEntry    = ttk.Entry(industrialBuildingWindow,  textvariable = buildingNameEntryVar)
    buildingNameEntry.grid(row = 1, column = 1, sticky = "we")
    
    ### Row 2 ###
    buildingHeightLabel = ttk.Label(industrialBuildingWindow, text = "Building height [m]", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingHeightLabel.grid(row = 2, column = 0)
    
    buildingHeightEntryVar = tk.DoubleVar()
    buildingHeightEntryVar.set(10.0)
    buildingHeightEntry    = ttk.Entry(industrialBuildingWindow,  textvariable = buildingHeightEntryVar)
    buildingHeightEntry.grid(row = 2, column = 1, sticky = "we")
    
    ### Row 3 ###
    buildingSurfaceLabel = ttk.Label(industrialBuildingWindow, text = "Building surface [m2]", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingSurfaceLabel.grid(row = 3, column = 0)
    
    buildingSurfaceEntryVar = tk.DoubleVar()
    buildingSurfaceEntryVar.set(100.0)
    buildingSurfaceEntry    = ttk.Entry(industrialBuildingWindow,  textvariable = buildingHeightEntryVar)
    buildingSurfaceEntry.grid(row = 3, column = 1, sticky = "we")
    
    ### Row 4 ###
    buildingFireResistanceCoefLabel = ttk.Label(industrialBuildingWindow, text = "Building Fire Resistance Coef.", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingFireResistanceCoefLabel.grid(row = 4, column = 0)
    
    buildingFireResistanceCoefList    = [">=R60", ">=R30", "<R30"]
    buildingFireResistanceCoefTextVar = tk.StringVar()
    buildingFireResistanceCoefTextVar.set(">=R60")
    buildingFireResistanceCoefCombobox = ttk.Combobox(industrialBuildingWindow, values = buildingFireResistanceCoefList, textvariable = buildingFireResistanceCoefTextVar)
    buildingFireResistanceCoefCombobox.grid(row = 4, column = 1, sticky = "we")
    
    ### Row 5 ###
    hazardousMaterialLabel = ttk.Label(industrialBuildingWindow, text = "Is there hazardous material in the building ?", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    hazardousMaterialLabel.grid(row = 5, column = 0)
    
    frameRow4 = ttk.Frame(industrialBuildingWindow)
    frameRow4.grid(row = 5, column = 1)
    
    hazardousMaterialVar = tk.BooleanVar()
    hazardousMaterialVar.set(True)
    hazardousMaterialRadioTrue  = ttk.Radiobutton(frameRow4, text = "True", variable = hazardousMaterialVar, value = True)
    hazardousMaterialRadioFalse = ttk.Radiobutton(frameRow4, text = "False", variable = hazardousMaterialVar, value = False)
            
    hazardousMaterialRadioTrue.grid(row = 0, column = 0, padx = 5)
    hazardousMaterialRadioFalse.grid(row = 0, column = 1, padx = 5)
    
    ### Row 6 ###
    buildingInterventionTypeCoefLabel = ttk.Label(industrialBuildingWindow, text = "Internal intervention method", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingInterventionTypeCoefLabel.grid(row = 6, column = 0)
    
    buildingInterventionTypeCoefList    = ["24/7 Presence", "24/7 Generalized DAI", "24/7 Fire Intervention"]
    buildingInterventionTypeCoefTextVar = tk.StringVar()
    buildingInterventionTypeCoefTextVar.set("24/7 Presence")
    buildingInterventionTypeCoefCombobox = ttk.Combobox(industrialBuildingWindow, values = buildingInterventionTypeCoefList, textvariable = buildingInterventionTypeCoefTextVar)
    buildingInterventionTypeCoefCombobox.grid(row = 6, column = 1, sticky = "we")
    
    ### Row 7 ###
    frameRow6 = ttk.Frame(industrialBuildingWindow)
    frameRow6.grid(row = 7, column = 0)
    
    buildingRiskCatLabel = ttk.Label(frameRow6, text = "Risk category", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    buildingRiskCatLabel.grid(row = 0, column = 0)
    buildingRiskCatAdvice = ttk.Label(frameRow6, text = "Check \"Appendice A\" from CNPP D9 document", font = ("TkDefaultFont", 10, "italic"), foreground = hydrogainBlue)
    buildingRiskCatAdvice.grid(row = 1, column = 0) 
    
    
    buildingRiskCatList    = ["RF", "1", "2", "3"]
    buildingRiskCatTextVar = tk.StringVar()
    buildingRiskCatTextVar.set("RF")
    buildingRiskCatCombobox = ttk.Combobox(industrialBuildingWindow, values = buildingRiskCatList, textvariable = buildingRiskCatTextVar)
    buildingRiskCatCombobox.grid(row = 7, column = 1, sticky = "we")
    
    ### Row 8 ###
    style = ttk.Style()
    style.configure("Green.TButton", font=("TkDefaultFont", 12, "bold"), foreground = hydrogainGreen)
    
    calculateRow7Button = ttk.Button(industrialBuildingWindow, text = "CREATE BUILDING", style = "Green.TButton", command = createIndustrialBuildingButton)
    calculateRow7Button.grid(row = 8, column = 0, columnspan = 2, sticky = "nswe", padx = 30, pady = 5, ipady = 10)
    
    ### Row 9 ###
    style = ttk.Style()
    style.configure("Red.TButton", font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    
    calculateButton = ttk.Button(industrialBuildingWindow, text = "CALCULATE", style = "Red.TButton", command = calculationButton)
    calculateButton.grid(row = 9, column = 0, columnspan = 2, sticky = "nswe", padx = 30, pady = 5, ipady = 10)
    
    ### Row 10 ###
    style = ttk.Style()
    style.configure("HGBlue.TButton", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    
    createBuildingButton = ttk.Button(industrialBuildingWindow, text = "GENERATE LaTeX", style = "HGBlue.TButton", command = generateLaTexFile)
    createBuildingButton.grid(row = 10, column = 0, columnspan = 2, sticky = "nswe", padx = 30, pady = 5, ipady = 10)
    
    
    
    ### RESULTS GUI ###
    calculationFrame = ttk.Frame(industrialBuildingWindow)
    calculationFrame.grid(row = 8, column = 2, rowspan = 3, sticky = "we", padx = 10, pady = 10)
    
    calculationFrame.rowconfigure(0, weight = 1)
    calculationFrame.rowconfigure(1, weight = 1)
    calculationFrame.rowconfigure(2, weight = 1)
    calculationFrame.rowconfigure(3, weight = 1)
    calculationFrame.rowconfigure(4, weight = 1)
    calculationFrame.rowconfigure(5, weight = 1)
    
    calculationFrame.columnconfigure(0, weight = 1)
    calculationFrame.columnconfigure(1, weight = 1)
    
    
    resultsLabel = ttk.Label(calculationFrame, text = "Results", font = ("TkDefaultFont", 16, "bold"), foreground = hydrogainBlue)
    resultsLabel.grid(row = 0, column = 0, columnspan = 2, padx = 30)    
    
    row7ButtonLabel1 = ttk.Label(calculationFrame, text = "Sum (All Coef.)", font = ("TkDefaultFont", 12, "italic"), foreground = hydrogainBlue)
    row7ButtonLabel1.grid(row = 1, column = 0, sticky = "w", padx = 30)
    sumCoef1Value = ttk.Label(calculationFrame, text = industrialBuildingObjectValue["sumCoef1"], font = ("TkDefaultFont", 12, "italic"), foreground = "Red")
    sumCoef1Value.grid(row = 1, column = 1)
    
    row7ButtonLabel2 = ttk.Label(calculationFrame, text = "1 + Sum (All Coef.)", font = ("TkDefaultFont", 12, "italic"), foreground = hydrogainBlue)
    row7ButtonLabel2.grid(row = 2, column = 0, sticky = "w", padx = 30)
    sumCoef2Value = ttk.Label(calculationFrame, text = industrialBuildingObjectValue["sumCoef2"], font = ("TkDefaultFont", 12, "italic"), foreground = "Red")
    sumCoef2Value.grid(row = 2, column = 1)
    
    row7ButtonLabel3 = ttk.Label(calculationFrame, text = "Interm. Flowrate [m3.h-1]", font = ("TkDefaultFont", 12, "italic"), foreground = hydrogainBlue)
    row7ButtonLabel3.grid(row = 3, column = 0, sticky = "w", padx = 30)
    intermFlowRateValue = ttk.Label(calculationFrame, text = industrialBuildingObjectValue["intermFlowRate"], font = ("TkDefaultFont", 12, "italic"), foreground = "Red")
    intermFlowRateValue.grid(row = 3, column = 1)
    
    row7ButtonLabel4 = ttk.Label(calculationFrame, text = "Current building Flowrate [m3.h-1]", font = ("TkDefaultFont", 12, "italic"), foreground = hydrogainBlue)
    row7ButtonLabel4.grid(row = 4, column = 0, sticky = "w", padx = 30)
    currentBuildingFlowRateValue = ttk.Label(calculationFrame, text = industrialBuildingObjectValue["currentBuildingFlowRate"], font = ("TkDefaultFont", 12, "italic"), foreground = "Red")
    currentBuildingFlowRateValue.grid(row = 4, column = 1)
    
    row7ButtonLabel5 = ttk.Label(calculationFrame, text = "Final Flowrate [m3.h-1]", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
    row7ButtonLabel5.grid(row = 5, column = 0, sticky = "w", padx = 30)
    finalFlowRateValue = ttk.Label(calculationFrame, text = industrialBuildingObjectValue["finalFlowRate"], font = ("TkDefaultFont", 12, "bold"), foreground = "Red")
    finalFlowRateValue.grid(row = 5, column = 1)

    

    ### SUMMARY ###
    canvasFrame = ttk.Frame(industrialBuildingWindow)
    canvasFrame.grid(row = 1, column = 2, rowspan = 7, sticky = "nswe", padx = 10)
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
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    