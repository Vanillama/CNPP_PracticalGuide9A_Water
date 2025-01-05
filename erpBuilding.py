class ErpBuilding:
    def __init__(self, name = "Building", buildingClass = "Class 1", surface = 100.0):
        self.name = name                    # Name of the building - String
        self.buildingClass = buildingClass  # Class of the building (Class 1 / Class 2 / Class 3 / Protected - String
        self.surface = surface              # Surface of the building - Float
    
        
    def flowRateCalculation(self):
        if (self.buildingClass == "Class 1"):
            if (self.surface <= 500.0):
                return ("60 m3/h")
            elif (self.surface <= 1000.0 and self.surface > 500.0):
                return ("60 m3/h")
            elif (self.surface <= 2000.0 and self.surface > 1000.0):
                return ("120 m3/h")
            elif (self.surface <= 3000.0 and self.surface > 2000.0):
                return ("180 m3/h")
            elif (self.surface <= 4000.0 and self.surface > 3000.0):
                return ("210 m3/h")
            elif (self.surface <= 5000.0 and self.surface > 4000.0):
                return ("240 m3/h")
            elif (self.surface <= 6000.0 and self.surface > 5000.0):
                return ("270 m3/h")
            elif (self.surface <= 7000.0 and self.surface > 6000.0):
                return ("300 m3/h")
            elif (self.surface <= 8000.0 and self.surface > 7000.0):
                return ("330 m3/h")
            elif (self.surface <= 9000.0 and self.surface > 8000.0):
                return ("360 m3/h")
            elif (self.surface <= 10000.0 and self.surface > 9000.0):
                return ("390 m3/h")
            elif (self.surface <= 20000.0 and self.surface > 10000.0):
                return ("To be handled on case by case basis")
            elif (self.surface <= 30000.0 and self.surface > 20000.0):
                return ("To be handled on case by case basis")
            else:
                return ("N/A")
        elif (self.buildingClass == "Class 2"):
            if (self.surface <= 500.0):
                return ("60 m3/h")
            elif (self.surface <= 1000.0 and self.surface > 500.0):
                return ("75 m3/h")
            elif (self.surface <= 2000.0 and self.surface > 1000.0):
                return ("150 m3/h")
            elif (self.surface <= 3000.0 and self.surface > 2000.0):
                return ("225 m3/h")
            elif (self.surface <= 4000.0 and self.surface > 3000.0):
                return ("270 m3/h")
            elif (self.surface <= 5000.0 and self.surface > 4000.0):
                return ("300 m3/h")
            elif (self.surface <= 6000.0 and self.surface > 5000.0):
                return ("330 m3/h")
            elif (self.surface <= 7000.0 and self.surface > 6000.0):
                return ("375 m3/h")
            elif (self.surface <= 8000.0 and self.surface > 7000.0):
                return ("420 m3/h")
            elif (self.surface <= 9000.0 and self.surface > 8000.0):
                return ("450 m3/h")
            elif (self.surface <= 10000.0 and self.surface > 9000.0):
                return ("480 m3/h")
            elif (self.surface <= 20000.0 and self.surface > 10000.0):
                return ("To be handled on case by case basis")
            elif (self.surface <= 30000.0 and self.surface > 20000.0):
                return ("To be handled on case by case basis")
            else:
                return ("N/A")
        elif (self.buildingClass == "Class 3"):
            if (self.surface <= 500.0):
                return ("60 m3/h")
            elif (self.surface <= 1000.0 and self.surface > 500.0):
                return ("90 m3/h")
            elif (self.surface <= 2000.0 and self.surface > 1000.0):
                return ("180 m3/h")
            elif (self.surface <= 3000.0 and self.surface > 2000.0):
                return ("270 m3/h")
            elif (self.surface <= 4000.0 and self.surface > 3000.0):
                return ("315 m3/h")
            elif (self.surface <= 5000.0 and self.surface > 4000.0):
                return ("360 m3/h")
            elif (self.surface <= 6000.0 and self.surface > 5000.0):
                return ("405 m3/h")
            elif (self.surface <= 7000.0 and self.surface > 6000.0):
                return ("450 m3/h")
            elif (self.surface <= 8000.0 and self.surface > 7000.0):
                return ("495 m3/h")
            elif (self.surface <= 9000.0 and self.surface > 8000.0):
                return ("540 m3/h")
            elif (self.surface <= 10000.0 and self.surface > 9000.0):
                return ("585 m3/h")
            elif (self.surface <= 20000.0 and self.surface > 10000.0):
                return ("To be handled on case by case basis")
            elif (self.surface <= 30000.0 and self.surface > 20000.0):
                return ("To be handled on case by case basis")
            else:
                return ("N/A")
        elif (self.buildingClass == "Protected"):
            if (self.surface <= 500.0):
                return ("60 m3/h")
            elif (self.surface <= 1000.0 and self.surface > 500.0):
                return ("60 m3/h")
            elif (self.surface <= 2000.0 and self.surface > 1000.0):
                return ("120 m3/h")
            elif (self.surface <= 3000.0 and self.surface > 2000.0):
                return ("180 m3/h")
            elif (self.surface <= 4000.0 and self.surface > 3000.0):
                return ("180 m3/h")
            elif (self.surface <= 5000.0 and self.surface > 4000.0):
                return ("240 m3/h")
            elif (self.surface <= 6000.0 and self.surface > 5000.0):
                return ("240 m3/h")
            elif (self.surface <= 7000.0 and self.surface > 6000.0):
                return ("240 m3/h")
            elif (self.surface <= 8000.0 and self.surface > 7000.0):
                return ("240 m3/h")
            elif (self.surface <= 9000.0 and self.surface > 8000.0):
                return ("240 m3/h")
            elif (self.surface <= 10000.0 and self.surface > 9000.0):
                return ("240 m3/h")
            elif (self.surface <= 20000.0 and self.surface > 10000.0):
                return ("300 m3/h")
            elif (self.surface <= 30000.0 and self.surface > 20000.0):
                return ("360 m3/h")
            else:
                return ("N/A")

    def fireHydrantPointsCalculation(self):
        if (self.buildingClass == "Class 1"):
            return ("According to the required overall flow rate and distribution based on the geometry of the buildings")
        elif (self.buildingClass == "Class 2"):
            return ("According to the required overall flow rate and distribution based on the geometry of the buildings")
        elif (self.buildingClass == "Class 3"):
            return ("According to the required overall flow rate and distribution based on the geometry of the buildings")
        elif (self.buildingClass == "Protected"):
            return ("According to the required overall flow rate and distribution based on the geometry of the buildings")
    
    def distanceFireHydrantPoints(self):
        if (self.buildingClass == "Class 1"):
            return ("200 m")
        elif (self.buildingClass == "Class 2"):
            return ("200 m")
        elif (self.buildingClass == "Class 3"):
            return ("200 m")
        elif (self.buildingClass == "Protected"):
            return ("200 m")
    
    def distanceFireHydrantEntrance(self):
        if (self.buildingClass == "Class 1"):
            return ("150 m (Dry Standpipe = 60 m)")
        elif (self.buildingClass == "Class 2"):
            return ("150 m (Dry Standpipe = 60 m)")
        elif (self.buildingClass == "Class 3"):
            return ("100 m (Dry Standpipe = 60 m)")
        elif (self.buildingClass == "Protected"):
            return ("150 m (Dry Standpipe = 60 m)")
    
    def minimalDurationCalculation(self):
        if (self.buildingClass == "Class 1"):
            return ("Unless otherwise specified, the minimum duration for the application of water requirements must be 2 hours.")
        elif (self.buildingClass == "Class 2"):
            return ("Unless otherwise specified, the minimum duration for the application of water requirements must be 2 hours.")
        elif (self.buildingClass == "Class 3"):
            return ("Unless otherwise specified, the minimum duration for the application of water requirements must be 2 hours.")
        elif (self.buildingClass == "Protected"):
            return ("Unless otherwise specified, the minimum duration for the application of water requirements must be 2 hours.")
    
        
    
    def __str__(self):
        return f"""
    The building type is an ERP building of {self.buildingClass}.
    The surface of the building is {self.surface} m2.
    _____________________________________________________________________________________________________"""
    
    def __repr__(self):
        return f"""ErpBuilding(name = {self.name}, buildingClass = {self.buildingClass}, surface = {self.surface})
    _____________________________________________________________________________________________________"""

