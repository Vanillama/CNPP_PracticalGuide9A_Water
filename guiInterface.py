import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


##### Main window initialisation #####
mainWindow = tk.Tk()


### Upload resources ###
hydrogainLogo_Square    = ImageTk.PhotoImage(Image.open("Resources/Images/HydroGainLogo_Square.png"))
hydrogainLogo_Rectangle = ImageTk.PhotoImage(Image.open("Resources/Images/HydroGainLogo_Rectangle.png"))
hydrogainLogo_SquareNT  = ImageTk.PhotoImage(Image.open("Resources/Images/HydroGainLogo_NoText.png"))

officeLogo              = ImageTk.PhotoImage(Image.open("Resources/Images/OfficeBuilding.png"))
erpLogo                 = ImageTk.PhotoImage(Image.open("Resources/Images/ERP.png"))
factpryLogo             = ImageTk.PhotoImage(Image.open("Resources/Images/Factory2.png"))


CNPP_D9Image            = ImageTk.PhotoImage(Image.open("Resources/Images/CNPP_D9.png").resize((200, 200)))
CNPP_D9AImage           = ImageTk.PhotoImage(Image.open("Resources/Images/CNPP_D9A.png").resize((200, 200)))

### Colours ###
hydrogainBlue  = "#263A91"
hydrogainGreen = "#A1CA18"

styleTitle = ttk.Style()
styleTitle.configure("titleLabel", font=("TkDefaultFont", 16, "bold"), foreground = hydrogainBlue)


##### Main window configuration #####
mainWindow.title("CNPP Practical Guide D9 / D9A")
mainWindow.iconbitmap("Resources/Images/HydroGainLogo_NoText.ico")

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


screenWidth  = mainWindow.winfo_screenwidth()*0.5
screenHeight = mainWindow.winfo_screenheight()*0.5

mainWindow.geometry(str(int(screenWidth)) + "x" + str(int(screenHeight)))


### FUNCTION ###
def openCNPPD9():
    cnppD9Window = tk.Toplevel(mainWindow)
    cnppD9Window.title("CNPP Practical Guide D9")
    cnppD9Window.geometry(str(int(screenWidth)) + "x" + str(int(screenHeight)))
    
def openCNPPD9A():
    cnppD9AWindow = tk.Toplevel(mainWindow)
    cnppD9AWindow.title("CNPP Practical Guide D9A")
    cnppD9AWindow.geometry(str(int(screenWidth)) + "x" + str(int(screenHeight)))


### Row 1 ###
mainTitle = ttk.Label(mainWindow, text = "CNPP Practical Guide D9 / D9A", font = ("TkDefaultFont", 16, "bold"), foreground = hydrogainBlue)
mainTitle.grid(row = 0, column = 0, columnspan = 5)

### Row 2 ###
buttonD9Title = ttk.Label(mainWindow, text = "CNPP Practical Guide D9", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
buttonD9Title.grid(row = 1, column = 1)

buttonD9ATitle = ttk.Label(mainWindow, text = "CNPP Practical Guide D9A", font = ("TkDefaultFont", 12, "bold"), foreground = hydrogainBlue)
buttonD9ATitle.grid(row = 1, column = 3)

### Row 3 ###
buttonD9  = ttk.Button(mainWindow, image = CNPP_D9Image, command = openCNPPD9)
buttonD9.grid(row = 2, column = 1, sticky = "nsew", padx = 30)

buttonD9A = ttk.Button(mainWindow, image = CNPP_D9AImage, command = openCNPPD9A)
buttonD9A.grid(row = 2, column = 3, sticky = "nsew", padx = 30)

### Row 4 ###
footNote = ttk.Label(mainWindow, text = "2024 - Guillaume THIRIET", font = ("Times", 10, "italic"))
footNote.grid(row = 4, column = 0, columnspan = 5, sticky = "se")



mainWindow.mainloop()