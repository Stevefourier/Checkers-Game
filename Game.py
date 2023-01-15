#*********************************************************************************************************#
#     Final Exam                                                                                          #
#     Name: Stephen Nwagwughiagwu 00743211                                                                #  
#     Description:This class manages the game and it utilizes the methods of the Board Class              #                                                                                 #
#******************************************************************************************************** #
from Board import Board #Importing the board class from the
from copy import deepcopy


#This class will be the main class that will manage the game and it utilizes the methods of the Board Class.
class Game:
    def __init__(self, board, move=None, parent=None, value=None): #Game class constructor that initializes properties of the Game Class
        self.board = board #Initializing the board property
        self.value = value 
        self.move = move
        self.parent = parent
        
        
    #Method to decide if a piece will become a KingedPiece and set the Type of the Piece with "X" or "O"
    def get_children(self, minimizing_player, mandatory_jumping):
        current_state = deepcopy(self.board) #Using the deepcopy method to initialize the current state of the checker board
        checkObj = Board() #Instantiating an object of the Board Class
        moves_avail = []
        statesCh = []
        kinged_Letter = ""
        kingedpc_row = 0
        if minimizing_player is True:
            moves_avail = Board.find_player2_moves_avail(current_state, mandatory_jumping)
            kinged_Letter = "X" #Assigning the piece to be a Kinged Piece "X"
            kingedpc_row = 7
        else:
            moves_avail = Board.find_player1_moves_avail(current_state, mandatory_jumping)
            kinged_Letter = "O" #Assigning the piece to be a Kinged Piece "O"
            kingedpc_row = 0
        for i in range(len(moves_avail)):
            old_i = moves_avail[i][0] #indexing through the location of the pieces in the list of lists which contains available moves to allow the player make the move
            old_j = moves_avail[i][1]
            new_i = moves_avail[i][2]
            new_j = moves_avail[i][3]
            state = deepcopy(current_state)
            checkObj.make_a_move(state, old_i, old_j, new_i, new_j, kinged_Letter, kingedpc_row)
            statesCh.append(Game(state, [old_i, old_j, new_i, new_j]))
        return statesCh

    def set_value(self, value): #This method sets the value of each of the piece
        self.value = value

    def get_value(self): #This method gets the value of each of each
        return self.value

    def get_board(self):
        return self.board

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent