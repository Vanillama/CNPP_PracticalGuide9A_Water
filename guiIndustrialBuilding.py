import tkinter as tk
import numpy as np
from tkinter import ttk
from PIL import Image, ImageTk



##### Residential Building window initialisation #####
def industrialBuildingWindow(rootWindow, screenWidth, screenHeight):
    industrialBuildingWindow = tk.Toplevel(rootWindow)
    industrialBuildingWindow.title("CNPP Practical Guide - Industrial Building")
    industrialBuildingWindow.iconbitmap("Resources/Images/HydroGainLogo_NoText.ico")
    industrialBuildingWindow.geometry(str(int(screenWidth)) + "x" + str(int(screenHeight)))