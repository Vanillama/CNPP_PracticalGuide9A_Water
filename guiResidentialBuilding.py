import tkinter as tk
import numpy as np
from tkinter import ttk
from PIL import Image, ImageTk



##### Residential Building window initialisation #####
def residentialBuildingWindow(rootWindow, screenWidth, screenHeight):
    residentialBuildingWindow = tk.Toplevel(rootWindow)
    residentialBuildingWindow.title("CNPP Practical Guide - Residential Building")
    residentialBuildingWindow.iconbitmap("Resources/Images/HydroGainLogo_NoText.ico")
    residentialBuildingWindow.geometry(str(int(screenWidth)) + "x" + str(int(screenHeight)))