class IndustrialBuilding:
    def __init__(self, name = "Building", height = 10.0, surface = 100.0, fireResistance = ">=R60", hazardousMaterial = True, internalInterventionType = "24/7 Presence", riskCategory = "2", autoWaterExtinctDevc = True):
        self.name = name                                          # Name of the building - String
        self.height = height                                      # Height of the building - Float
        self.surface = surface                                    # Surface of the building - Float
        self.fireResistance = fireResistance                      # Mechanical fire resistance of the building structure (>=R60 / >=R30 / <R30) - String 
        self.hazardousMaterial = hazardousMaterial                # Presence of the hazardous material - Boolean
        self.internalInterventionType = internalInterventionType  # Type of intervention (N/A / 24/7 Presence / 24/7 Generalized DAI / 24/7 Fire Intervention) - String
        self.riskCategory = riskCategory                          # Category of the risk (RF / 1 / 2 / 3) - String
        self.autoWaterExtinctDevc = autoWaterExtinctDevc          # Automatic water extinction device - Boolean
        
    
    def heightCoef(self):
        if (self.height <= 3.0):
            return (0.0)
        elif (self.height <= 8.0 and self.height > 3.0):
            return (0.1)
        elif (self.height <= 12.0 and self.height > 8.0):
            return (0.2)
        elif (self.height <= 30.0 and self.height > 12.0):
            return (0.5)
        elif (self.height <= 40.0 and self.height > 30.0):
            return (0.7)
        elif (self.height > 40.0):
            return (0.8)
        
    def fireResistanceCoef(self):
        if (self.fireResistance == ">=R60"):
            return (-0.1)
        elif (self.fireResistance == ">=R30"):
            return (0.0)
        elif (self.foreResistance == "<R30"):
            return (0.1)
    
    def hazardousMaterialCoef(self):
        if (self.hazardousMaterial == True):
            return (0.1)
        else:
            return (0.0)
        
    def internalInterventionTypeCoef(self):
        if (self.internalInterventionType == "24/7 Presence"):
            return (-0.1)
        elif (self.internalInterventionType == "24/7 Generalized DAI"):
            return (-0.1)
        elif (self.internalInterventionType == "24/7 Fire Intervention"):
            return (-0.3)
        else:
            return (0.0)
        
    def sumCoef1(self):
        return (self.heightCoef() + self.fireResistanceCoef() + self.hazardousMaterialCoef() + self.internalInterventionTypeCoef())
    
    def sumCoef2(self):
        return (1.0 + self.heightCoef() + self.fireResistanceCoef() + self.hazardousMaterialCoef() + self.internalInterventionTypeCoef())
    
    def intermFlowRate(self):
        return (30.0 * (self.surface / 500.0) * self.sumCoef2())
    
    def riskCategoryCoef(self):
        if (self.riskCategory == "RF"):
            return (self.intermFlowRate() * 0.5)
        elif (self.riskCategory == "1"):
            return (self.intermFlowRate() * 1.0)
        elif (self.riskCategory == "2"):
            return (self.intermFlowRate() * 1.5)
        elif (self.riskCategory == "3"):
            return (self.intermFlowRate() * 2.0)
        
    def autoWaterExtinctCoef(self):
        if (self.autoWaterExtinctDevc == True):
            return (self.riskCategoryCoef() / 2.0)
        else:
            return (self.riskCategoryCoef())



    def __str__(self):
        return f"""
    The building type is an industrial building of risk category : {self.riskCategory}.
    The building is {self.height} meters high. The surface of the building is {self.surface} m2. 
    The fire resistance of the mechanical structure of the building is {self.fireResistance}.
    The building contains hazardous materials : {self.hazardousMaterial}.
    The type of internal intervention is : {self.internalInterventionType}.
    The building is equipped with a fire safety system : {self.autoWaterExtinctDevc}.
    _____________________________________________________________________________________________"""
    
    def __repr__(self):
        return f"""IndustrialBuilding(name = {self.name}, height = {self.height}, surface = {self.surface}, fireResistance = {self.fireResistance}, hazardousMaterial = {self.hazardousMaterial}, internalInterventionType = {self.internalInterventionType}, 
    riskCategory = {self.riskCategory}, autoWaterExtinctDevc = {self.autoWaterExtinctDevc})
    _____________________________________________________________________________________________"""
