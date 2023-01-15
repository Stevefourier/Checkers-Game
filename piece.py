#*********************************************************************************************************#
#     Final Exam                                                                                          #
#     Name: Stephen Nwagwughiagwu 00743211                                                                #  
#     Description:This class will be the main class that will manage the game and it utilizes the methods # 
#     of the Board Class                                                                                  #
#******************************************************************************************************** #
#This Class captures the state of an individual piece and will be used by the Board Class to control 
class Piece:
    def __init__(self): #Constructor for the piece class with the properties instantiated
        self.locRow = "" #Indicates Row Location
        self.locCol = 0   #Indicates the column location
        self.pcType = "" #Indicates the Norm or Kinged piece ('x','o','X' or 'O')

    def setLoc(self, locRow, locCol): #This method sets the location
        self.locRow = locRow 
        self.locCol = locCol  
    
    def getLoc(self): #Returns the location
        return [self.locRow, self.locCol]
    
    def setType(self, pcType): #Method that sets the piece type
        self.pcType = pcType
    
    def getType(self): #This will return the piece type
        return self.pcType