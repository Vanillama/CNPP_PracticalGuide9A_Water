import tkinter as tk
import numpy as np
from tkinter import ttk
from PIL import Image, ImageTk



##### Residential Building window initialisation #####
def officeBuildingWindow(rootWindow, screenWidth, screenHeight):
    officeBuildingWindow = tk.Toplevel(rootWindow)
    officeBuildingWindow.title("CNPP Practical Guide - Office Building")
    officeBuildingWindow.iconbitmap("Resources/Images/HydroGainLogo_NoText.ico")
    officeBuildingWindow.geometry(str(int(screenWidth)) + "x" + str(int(screenHeight)))
