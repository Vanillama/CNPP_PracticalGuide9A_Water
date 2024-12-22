import tkinter as tk
import numpy as np
from tkinter import ttk
from PIL import Image, ImageTk



##### Residential Building window initialisation #####
def erpBuildingWindow(rootWindow, screenWidth, screenHeight):
    erpBuildingWindow = tk.Toplevel(rootWindow)
    erpBuildingWindow.title("CNPP Practical Guide - ERP Building")
    erpBuildingWindow.iconbitmap("Resources/Images/HydroGainLogo_NoText.ico")
    erpBuildingWindow.geometry(str(int(screenWidth)) + "x" + str(int(screenHeight)))