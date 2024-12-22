class OfficeBuilding:
    
    def __init__(self, name = "Building", height = 10.0, surface = 100.0):
        self.name = name       # Name of the building - String
        self.height = height   # Height of the building - Float
        self.surface = surface # Surface of the building - Float
        
    
    def flowRateCalculation(self):
        if (self.height <= 8.0 and self.surface <= 500):
            return ("See the rules set out in the departmental regulations for external fire protection...")
        elif (((self.height <= 28.0) and (self.height > 8.0)) and (self.surface <= 2000.0)):
            return ("120 m3.h-1")
        elif (((self.height <= 28.0) and (self.height > 8.0)) and ((self.surface <= 5000.0) and (self.surface > 2000.0))):
            return ("180 m3.h-1")
        elif (self.surface > 5000.0):
            return ("240 m3.h-1")
         
    def fireHydrantPointsCalculation(self):
        if (self.height <= 8.0 and self.surface <= 500):
            return ("See the rules set out in the departmental regulations for external fire protection...")
        elif (((self.height <= 28.0) and (self.height > 8.0)) and (self.surface <= 2000.0)):
            return ("2 of 100 mm")
        elif (((self.height <= 28.0) and (self.height > 8.0)) and ((self.surface <= 5000.0) and (self.surface > 2000.0))):
            return ("3 of 100 mm")
        elif (self.surface > 5000.0):
            return ("2 of 100 mm AND 1 of 2*100 mm (referred to as 150 mm)")
    
    def distanceFireHydrantPoints(self):
        if (self.height <= 8.0 and self.surface <= 500):
            return ("See the rules set out in the departmental regulations for external fire protection...")
        elif (((self.height <= 28.0) and (self.height > 8.0)) and (self.surface <= 2000.0)):
            return ("200 m")
        elif (((self.height <= 28.0) and (self.height > 8.0)) and ((self.surface <= 5000.0) and (self.surface > 2000.0))):
            return ("200 m")
        elif (self.surface > 5000.0):
            return ("200 m")
    
    def distanceFireHydrantEntrance(self):
        if (self.height <= 8.0 and self.surface <= 500):
            return ("See the rules set out in the departmental regulations for external fire protection...")
        elif (((self.height <= 28.0) and (self.height > 8.0)) and (self.surface <= 2000.0)):
            return ("150 m")
        elif (((self.height <= 28.0) and (self.height > 8.0)) and ((self.surface <= 5000.0) and (self.surface > 2000.0))):
            return ("100 m (Dry Riser = 60 m)")
        elif (self.surface > 5000.0):
            return ("100 m (Dry Riser = 60 m)")
    
    def minimalDurationCalculation(self):
        if (self.height <= 8.0 and self.surface <= 500):
            return ("See the rules set out in the departmental regulations for external fire protection...")
        elif (((self.height <= 28.0) and (self.height > 8.0)) and (self.surface <= 2000.0)):
            return ("Unless otherwise specified, the minimum duration for the application of water requirements must be 2 hours.")
        elif (((self.height <= 28.0) and (self.height > 8.0)) and ((self.surface <= 5000.0) and (self.surface > 2000.0))):
            return ("Unless otherwise specified, the minimum duration for the application of water requirements must be 2 hours.")
        elif (self.surface > 5000.0):
            return ("Unless otherwise specified, the minimum duration for the application of water requirements must be 2 hours.")
        
    
    
    def __str__(self):
        return f"""The building type is an office building.
    The building is {self.height} meters high. The surface of the building is {self.surface} m2."""
    
    def __repr__(self):
        return f"""OfficeBuilding(name = {self.name}, height = {self.height}, surface = {self.surface})"""
        

