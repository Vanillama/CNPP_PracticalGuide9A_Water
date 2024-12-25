import tkinter as tk
from guiResidentialBuilding import residentialBuildingWindow
from guiOfficeBuilding import officeBuildingWindow
from guiERPBuilding import erpBuildingWindow
from guiIndustrialBuilding import industrialBuildingWindow
from guiCredits import creditsWindow

from tkinter import ttk
from PIL import Image, ImageTk



##### Main window initialisation #####
mainWindow = tk.Tk()


### Upload resources ###
hydrogainLogo_Square    = ImageTk.PhotoImage(Image.open("Resources/Images/HydroGainLogo_Square.png"))
hydrogainLogo_Rectangle = ImageTk.PhotoImage(Image.open("Resources/Images/HydroGainLogo_Rectangle.png"))
hydrogainLogo_SquareNT  = ImageTk.PhotoImage(Image.open("Resources/Images/HydroGainLogo_NoText.png"))

cnppLogo_Simple         = ImageTk.PhotoImage(Image.open("Resources/Images/CNPPLogo_Simple.png").resize((210, 125)))
cnppLogo_Complex        = ImageTk.PhotoImage(Image.open("Resources/Images/CNPPLogo_Complex.png").resize((185, 125)))

residentialLogo         = ImageTk.PhotoImage(Image.open("Resources/Images/ResidentialBuilding.png").resize((125, 125)))
officeLogo              = ImageTk.PhotoImage(Image.open("Resources/Images/OfficeBuilding.png").resize((125, 125)))
erpLogo                 = ImageTk.PhotoImage(Image.open("Resources/Images/ERP.png").resize((125, 125)))
factoryLogo             = ImageTk.PhotoImage(Image.open("Resources/Images/Factory.png").resize((125, 125)))

CNPP_D9Image            = ImageTk.PhotoImage(Image.open("Resources/Images/CNPP_D9.png").resize((75, 75)))
CNPP_D9AImage           = ImageTk.PhotoImage(Image.open("Resources/Images/CNPP_D9A.png").resize((75, 75)))


### Colours ###
hydrogainBlue  = "#263A91"
hydrogainGreen = "#A1CA18"

styleTitle = ttk.Style()
styleTitle.configure("titleLabel", font=("TkDefaultFont", 20, "bold"), foreground = hydrogainBlue)



##### Main window configuration #####
mainWindow.title("CNPP Practical Guide D9 / D9A")
#mainWindow.iconbitmap("Resources/Images/HydroGainLogo_NoText.ico")
mainWindow.iconbitmap("Resources/Images/CNPPLogo_Simple.ico")

mainWindow.rowconfigure(0, weight = 1)
mainWindow.rowconfigure(1, weight = 1)
mainWindow.rowconfigure(2, weight = 2)
mainWindow.rowconfigure(3, weight = 1)
mainWindow.rowconfigure(4, weight = 1)

mainWindow.columnconfigure(0, weight = 1)
mainWindow.columnconfigure(1, weight = 1)
mainWindow.columnconfigure(2, weight = 1)
mainWindow.columnconfigure(3, weight = 1)
mainWindow.columnconfigure(4, weight = 1)
mainWindow.columnconfigure(5, weight = 1)
mainWindow.columnconfigure(6, weight = 1)
mainWindow.columnconfigure(7, weight = 1)


screenWidth  = mainWindow.winfo_screenwidth()*0.5
screenHeight = mainWindow.winfo_screenheight()*0.5

mainWindow.geometry(str(int(screenWidth)) + "x" + str(int(screenHeight)))



### FUNCTIONS ###
def openResidentialBuildWin():
    residentialBuildingWindow(mainWindow, screenWidth, screenHeight)
    
def openOfficeBuildWin():
    officeBuildingWindow(mainWindow, screenWidth, screenHeight)
    
def openERPBuildWin():
    erpBuildingWindow(mainWindow, screenWidth, screenHeight)
    
def openIndustrialBuildWin():
    industrialBuildingWindow(mainWindow, screenWidth, screenHeight)
    
def openCredits():
    creditsWindow(mainWindow, screenWidth, screenHeight, {"cnppD9" : CNPP_D9Image, "cnppD9A" : CNPP_D9AImage, "residentialImage" : residentialLogo, "officeImage" : officeLogo, "erpImage" : erpLogo, "industrialImage" : factoryLogo})  



### Row 0 ###
mainTitle = ttk.Label(mainWindow, text = "CNPP Practical Guide D9 / D9A", font = ("TkDefaultFont", 16, "bold"), foreground = hydrogainBlue)
mainTitle.grid(row = 0, column = 0, columnspan = 8)


### Row 1 ###
buttonResidentialBuildTitle = ttk.Label(mainWindow, text = "Residential Building", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
buttonResidentialBuildTitle.grid(row = 1, column = 1, sticky = "s")

buttonOfficeBuildTitle = ttk.Label(mainWindow, text = "Office Building", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
buttonOfficeBuildTitle.grid(row = 1, column = 3, sticky = "s")

buttonERPBuildTitle = ttk.Label(mainWindow, text = "ERP Building", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
buttonERPBuildTitle.grid(row = 1, column = 5, sticky = "s")

buttonIndustrialBuildTitle = ttk.Label(mainWindow, text = "Industrial Building", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
buttonIndustrialBuildTitle.grid(row = 1, column = 7, sticky = "s")


### Row 2 ###
buttonResidentialBuild  = ttk.Button(mainWindow, image = residentialLogo, command = openResidentialBuildWin, padding = 30)
buttonResidentialBuild.grid(row = 2, column = 1, padx = 30)

buttonOfficeBuild = ttk.Button(mainWindow, image = officeLogo, command = openOfficeBuildWin, padding = 30)
buttonOfficeBuild.grid(row = 2, column = 3, padx = 30)

buttonERPBuild = ttk.Button(mainWindow, image = erpLogo, command = openERPBuildWin, padding = 30)
buttonERPBuild.grid(row = 2, column = 5, padx = 30)

buttonIndustrialBuild = ttk.Button(mainWindow, image = factoryLogo, command = openIndustrialBuildWin, padding = 30)
buttonIndustrialBuild.grid(row = 2, column = 7, padx = 30)


### Row 3 ###
frame = ttk.Frame(mainWindow)
frame.grid(row = 3, column = 0, columnspan = 4, sticky = "nsew")

backgroundLabelLogo = ttk.Label(frame, image = cnppLogo_Simple)
backgroundLabelD9 = ttk.Label(frame, image = CNPP_D9Image)
backgroundLabelD9A = ttk.Label(frame, image = CNPP_D9AImage)

backgroundLabelD9.grid(row = 0, column = 0, padx = 5)
backgroundLabelD9A.grid(row = 0, column = 1, padx = 5)
backgroundLabelLogo.grid(row = 0, column = 2, padx = 5)

style = ttk.Style()
style.configure("HGBlue.TButton", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)

creditsButton = ttk.Button(frame, text = "Credits", style = "HGBlue.TButton", command = openCredits)
creditsButton.grid(row = 1, column = 0, columnspan = 4, sticky = "nswe", padx = 5, pady = 5)


### Row 4 ###
footNote = ttk.Label(mainWindow, text = "2024 - Guillaume THIRIET", font = ("Times", 10, "italic"))
footNote.grid(row = 4, column = 7, columnspan = 2, sticky = "se")


mainWindow.mainloop()