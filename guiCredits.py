import tkinter as tk
from tkinter import ttk


### Colours ###
hydrogainBlue  = "#263A91"
hydrogainGreen = "#A1CA18"



##### Credits window initialisation #####
def creditsWindow(rootWindow, screenWidth, screenHeight, dictImages):
    
    creditsWindow = tk.Toplevel(rootWindow)
    creditsWindow.title("CNPP Practical Guide - Credits")
    #creditsWindow.iconbitmap("Resources/Images/HydroGainLogo_NoText.ico")
    creditsWindow.iconbitmap("Resources/Images/CNPPLogo_Simple.ico")
    creditsWindow.geometry(str(int(screenWidth*1.2)) + "x" + str(int(screenHeight*1.2)))
    
    creditsWindow.rowconfigure(0, weight = 1)
    creditsWindow.rowconfigure(1, weight = 1)
    creditsWindow.rowconfigure(2, weight = 1)
    creditsWindow.rowconfigure(3, weight = 1)
    creditsWindow.rowconfigure(4, weight = 1)
    creditsWindow.rowconfigure(5, weight = 1)
    
    creditsWindow.columnconfigure(0, weight = 1)
    creditsWindow.columnconfigure(1, weight = 5)
    
    ### Row 0 ###
    creditsTitle = ttk.Label(creditsWindow, text = "CREDITS", font = ("TkDefaultFont", 20, "bold"), foreground = hydrogainBlue)
    creditsTitle.grid(row = 0, column = 0, columnspan = 2)
    
    ### Row 1 ###
    cnppFrame = ttk.Frame(creditsWindow)
    cnppFrame.grid(row = 1, column = 0, padx = 50)
    
    cnppD9Image = ttk.Label(cnppFrame, image = dictImages["cnppD9"])
    cnppD9Image.grid(row = 0, column = 0)
    cnppD9AImage = ttk.Label(cnppFrame, image = dictImages["cnppD9A"])
    cnppD9AImage.grid(row = 0, column = 1)
    
    cnppText = """
    CNPP D9 - GUIDE PRATIQUE Appui au dimensionnement des besoins en eau pour la défense extérieure contre l’incendie. 06/2020
    CNPP D9A - GUIDE PRATIQUE Dimensionnement des rétentions des eaux d’extinction. 06/2020"""
    
    cnppTextLabel = ttk.Label(creditsWindow, text = cnppText)
    cnppTextLabel.grid(row = 1, column = 1, sticky = "w", padx = 10)
    
    ### Row 2 ###
    image1Text = """
    <a href="https://www.flaticon.com/free-icons/flats" title="flats icons">Flats icons created by Freepik - Flaticon</a>
    Free for personal and commercial purpose with attribution."""
    
    image1Label = ttk.Label(creditsWindow, image = dictImages["residentialImage"])
    image1Label.grid(row = 2, column = 0, padx = 50)
    
    image1Text = ttk.Label(creditsWindow, text = image1Text)
    image1Text.grid(row = 2, column = 1, sticky = "w", padx = 10)
    
    ### Row 3 ###
    image2Text = """
    <a href="https://www.flaticon.com/fr/icones-gratuites/urbain" title="urbain icônes">Urbain icônes créées par Zlatko Najdenovski - Flaticon</a>
    Free for personal and commercial purpose with attribution."""
    
    image2Label = ttk.Label(creditsWindow, image = dictImages["officeImage"])
    image2Label.grid(row = 3, column = 0, padx = 50)
    
    image2Text = ttk.Label(creditsWindow, text = image2Text)
    image2Text.grid(row = 3, column = 1, sticky = "w", padx = 10)
        
    ### Row 4 ###
    image3Text = """
    <a href="https://www.flaticon.com/free-icons/town-hall" title="town hall icons">Town hall icons created by Freepik - Flaticon</a>
    Free for personal and commercial purpose with attribution."""
    
    image3Label = ttk.Label(creditsWindow, image = dictImages["erpImage"])
    image3Label.grid(row = 4, column = 0, padx = 50)
    
    image3Text = ttk.Label(creditsWindow, text = image3Text)
    image3Text.grid(row = 4, column = 1, sticky = "w", padx = 10)
        
    ### Row 5 ###
    image4Text = """
    <a href="https://www.flaticon.com/free-icons/factory" title="factory icons">Factory icons created by Eucalyp - Flaticon</a>
    Free for personal and commercial purpose with attribution."""
    
    image4Label = ttk.Label(creditsWindow, image = dictImages["industrialImage"])
    image4Label.grid(row = 5, column = 0, padx = 50)
    
    image4Text = ttk.Label(creditsWindow, text = image4Text)
    image4Text.grid(row = 5, column = 1, sticky = "w", padx = 10)
       


    
