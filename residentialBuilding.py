class ResidentialBuilding:
    
    def __init__(self, name = "Building", buildingType = "individual", stageNmb = 1, height = 10.0, stairsDistance = 10.0, ladderTruckAccess = True):
        self.name = name                            # Name of the building - String
        self.buildingType = buildingType            # Type of building = individual / collective - String
        self.stageNmb = stageNmb                    # Number of stage in the building - Int
        self.height = height                        # Height of the building - Float
        self.stairsDistance = stairsDistance        # Distance between the stairs and the room - Float
        self.ladderTruckAccess = ladderTruckAccess  # Is there an access to the stairs from the ladder truck way - Boolean
    
    
    def buildingClass(self):
        buildingClass = "Class 1"
        
        if (self.buildingType == "individual" and self.stageNmb <= 1):
            buildingClass = "Class 1"
        elif((self.buildingType == "individual" and self.stageNmb > 1) or (self.buildingType == "collective" and self.stageNmb <= 3)):
            buildingClass = "Class 2"
        elif(self.buildingType == "collective" and self.height <= 28 and self.stageNmb <= 7 and self.stageNmb > 3 and self.stairsDistance <= 10.0 and self.ladderTruckAccess == True):
            buildingClass = "Class 3A"
        elif(self.buildingType == "collective" and self.height <= 28 and (self.stageNmb <= 7 and self.stairsDistance <= 10.0 and self.ladderTruckAccess == True) == False):
            buildingClass = "Class 3B"
        elif(self.buildingType == "collective" and self.height > 28 and self.height <= 50):
            buildingClass = "IMH"
        elif(self.buildingType == "collective" and self.height > 50):
            buildingClass = "IGH"       
        return (buildingClass)
    
    def flowRateCalculation(self):
        buildingClass = self.buildingClass()
        
        if ((buildingClass == "Class 1") or (buildingClass == "Class 2")):
            return ("See the rules set out in the departmental regulations for external fire protection...")
        if (buildingClass == "Class 3A"):
            return ("120 m3.h-1")
        if ((buildingClass == "Class 3B") or (buildingClass == "IMH") or (buildingClass == "IGH")):
            return ("120 m3.h-1")
        
    def fireHydrantPointsCalculation(self):
        buildingClass = self.buildingClass()
        
        if ((buildingClass == "Class 1") or (buildingClass == "Class 2")):
            return ("See the rules set out in the departmental regulations for external fire protection...")
        if (buildingClass == "Class 3A"):
            return ("2 of 100 mm")
        if ((buildingClass == "Class 3B") or (buildingClass == "IMH") or (buildingClass == "IGH")):
            return ("2 of 100 mm")
        
    def distanceFireHydrantPoints(self):
        buildingClass = self.buildingClass()
        
        if ((buildingClass == "Class 1") or (buildingClass == "Class 2")):
            return ("See the rules set out in the departmental regulations for external fire protection...")
        if (buildingClass == "Class 3A"):
            return ("200 m")
        if ((buildingClass == "Class 3B") or (buildingClass == "IMH") or (buildingClass == "IGH")):
            return ("200 m")
        
    def distanceFireHydrantEntrance(self):
        buildingClass = self.buildingClass()
        
        if ((buildingClass == "Class 1") or (buildingClass == "Class 2")):
            return ("See the rules set out in the departmental regulations for external fire protection...")
        if (buildingClass == "Class 3A"):
            return ("150 m")
        if ((buildingClass == "Class 3B") or (buildingClass == "IMH") or (buildingClass == "IGH")):
            return ("100 m (Dry Riser = 60 m)")
        
    def minimalDurationCalculation(self):
        buildingClass = self.buildingClass()
        
        if ((buildingClass == "Class 1") or (buildingClass == "Class 2")):
            return ("See the rules set out in the departmental regulations for external fire protection...")
        if (buildingClass == "Class 3A"):
            return ("Unless otherwise specified, the minimum duration for the application of water requirements must be 2 hours.")
        if ((buildingClass == "Class 3B") or (buildingClass == "IMH") or (buildingClass == "IGH")):
            return ("Unless otherwise specified, the minimum duration for the application of water requirements must be 2 hours.")
     
    
        
    def __str__(self):
        return f"""
    The building type is a residential \"{self.buildingType}\" building. 
    The building has {self.stageNmb} floors and is {self.height} meters high.
    The distance between the accomodation and the staircase is less than {self.stairsDistance} meters.
    There is a ladder truck access to the accomodation : {self.ladderTruckAccess}.
    _____________________________________________________________________________________________________"""
    
    def __repr__(self):
        return f"""ResidentialBuilding(name = {self.name}, buildingType = \"{self.buildingType}\", stageNmb = {self.stageNmb}, height = {self.height},
    stairsDistance = {self.stairsDistance}, ladderTruckAccess = {self.ladderTruckAccess})
    _____________________________________________________________________________________________________"""
        
        