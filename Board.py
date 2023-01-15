#*********************************************************************************************************#                                                                                         #
#     Name: Stephen Nwagwughiagwu                                                                         #  
#     Description: A Board Class module manages the pieces of the checker game at the board level          #
#******************************************************************************************************** #

import math
from copy import deepcopy

class Board:

    def __init__(self): #Constructor of the board class that initializes the properties of the Board Class
        self.matrix = [[], [], [], [], [], [], [], []] #List of list to diaplay the board with the grids
        self.player1_turn = True
        self.player2_turn = True
        self.player1_pieces = 12 #Instantiating the number of pieces per player
        self.player2_pieces = 12 ##Instantiating the number of pieces per player
        self.movAvail = [] #Instantiating list to store available moves
        self.jump = False

        for row in self.matrix:
            for i in range(8):
                row.append("-") #Creates the unoccupied grids in the board
                
        self.position_player2()
        self.position_player1()

    def position_player2(self): #Defining th position of Player 2
        for i in range(3):
            for j in range(8):
                if (i + j) % 2 == 1:
                    self.matrix[i][j] = ("x")
                else:
                    self.matrix[i][j] = ("-")

    def position_player1(self): #Defining the position of Player1 
        for i in range(5, 8, 1):
            for j in range(8):
                if (i + j) % 2 == 1:
                    self.matrix[i][j] = ("o")
                else:
                    self.matrix[i][j] = ("-")

    def printBoard(self): #This method prints the board to standard output
        i = 0
        print()
        for row in self.matrix:
            print(i, end="  |")
            i += 1
            for elem in row:
                print(elem, end=" ")
            print()
        print()
        for j in range(8):
            if j == 0:
                j = "    0"
            print(j, end=" ")
        print("\n")

    def get_player1_input(self):
        movAvail = Board.find_player1_movAvail(self.matrix, self.jump)
        if len(movAvail) == 0:
            if self.player2_pieces > self.player1_pieces:
                print("You have literally exhausted all your moves" )
                exit()
            else:
                print("No more moves available.\nGAME ENDED!")
                exit()
        self.player1_pieces = 0
        self.player2_pieces = 0
        while True:

            coord1 = input("Please Enter Your Move: Source [i,j]: ") #Collects source index of the piece to move
            if coord1 == "":
                print( "Game ended!")
                exit()
            coord2 = input("Please Enter Your Move: Destination [i,j]:") #Collects destination index of the piece to move
            if coord2 == "":
                print("Game ended!")
                exit()
            old = coord1.split(",") 
            new = coord2.split(",")

            if len(old) != 2 or len(new) != 2:
                print("Illegal input made")
            else:
                old_i = old[0]
                old_j = old[1]
                new_i = new[0]
                new_j = new[1]
                if not old_i.isdigit() or not old_j.isdigit() or not new_i.isdigit() or not new_j.isdigit():
                    print("Illegal input")
                else:
                    move = [int(old_i), int(old_j), int(new_i), int(new_j)]
                    if move not in movAvail:
                        print("Illegal move!")
                    else:
                        Board.make_a_move(self.matrix, int(old_i), int(old_j), int(new_i), int(new_j), "O", 0)
                        for m in range(8):
                            for n in range(8):
                                if self.matrix[m][n][0] == "x" or self.matrix[m][n][0] == "X":
                                    self.player2_pieces += 1
                                elif self.matrix[m][n][0] == "o" or self.matrix[m][n][0] == "O":
                                    self.player1_pieces += 1
                        break
    #Method to
    def get_player2_input(self):
        movAvail = Board.find_player2_movAvail(self.matrix, self.jump)
        if len(movAvail) == 0:
            if self.player1_pieces > self.player2_pieces:
                print("You have no moves left, and you have fewer pieces than the player2.YOU LOSE!")
                exit()
            else:
                print("You have no available moves.\nGAME ENDED!")
                exit()
        self.player1_pieces = 0
        self.player2_pieces = 0
        while True:

            coord1 = input("Please Enter Your Move: Source [i,j]: ")
            if coord1 == "":
                print("Game ended!")
                exit()
            coord2 = input("Please Enter Your Move: Destination [i,j]: ")
            if coord2 == "":
                print("Game ended!")
                exit()
            old = coord1.split(",")
            new = coord2.split(",")

            if len(old) != 2 or len(new) != 2:
                print("Illegal input")
            else:
                old_i = old[0] #
                old_j = old[1]
                new_i = new[0]
                new_j = new[1]
                if not old_i.isdigit() or not old_j.isdigit() or not new_i.isdigit() or not new_j.isdigit(): #Checks the input for source and destination move input is a number
                    print("Illegal input")
                else:
                    move = [int(old_i), int(old_j), int(new_i), int(new_j)]
                    if move not in movAvail:
                        print("Illegal move!")
                    else:
                        Board.make_a_move(self.matrix, int(old_i), int(old_j), int(new_i), int(new_j), "O", 0)
                        for m in range(8):
                            for n in range(8):
                                if self.matrix[m][n][0] == "x" or self.matrix[m][n][0] == "X":
                                    self.player2_pieces += 1
                                elif self.matrix[m][n][0] == "o" or self.matrix[m][n][0] == "O":
                                    self.player1_pieces += 1
                        break

    #Helper method to check moves available for player 1 and store them in a list
    def find_player2_movAvail(board, jump):
        movAvail = [] #List to store available moves for Player 2
        jumpAvail = [] # List to store available jump possibilities for Player 2
        for m in range(8):
            for n in range(8):
                if board[m][n][0] == "x": #Checks if the first grid in the board contains the "x" piecetype
                    if Board.check_player2_moves(board, m, n, m + 1, n + 1):
                        movAvail.append([m, n, m + 1, n + 1])
                    if Board.check_player2_moves(board, m, n, m + 1, n - 1):
                        movAvail.append([m, n, m + 1, n - 1])
                    if Board.check_player2_jumps(board, m, n, m + 1, n - 1, m + 2, n - 2):
                        jumpAvail.append([m, n, m + 2, n - 2])
                    if Board.check_player2_jumps(board, m, n, m + 1, n + 1, m + 2, n + 2):
                        jumpAvail.append([m, n, m + 2, n + 2])
                elif board[m][n][0] == "X": #Checks if the first grid in the board contains the "X" piecetype
                    if Board.check_player2_moves(board, m, n, m + 1, n + 1):
                        movAvail.append([m, n, m + 1, n + 1])
                    if Board.check_player2_moves(board, m, n, m + 1, n - 1): #
                        movAvail.append([m, n, m + 1, n - 1])
                    if Board.check_player2_moves(board, m, n, m - 1, n - 1):
                        movAvail.append([m, n, m - 1, n - 1])
                    if Board.check_player2_moves(board, m, n, m - 1, n + 1): #Calling the "check_player2_moves" function to verify the destination grid is eligible for a jump and appending it to the list of available jumps
                        movAvail.append([m, n, m - 1, n + 1])
                    if Board.check_player2_jumps(board, m, n, m + 1, n - 1, m + 2, n - 2): 
                        jumpAvail.append([m, n, m + 2, n - 2])
                    if Board.check_player2_jumps(board, m, n, m - 1, n - 1, m - 2, n - 2):
                        jumpAvail.append([m, n, m - 2, n - 2])
                    if Board.check_player2_jumps(board, m, n, m - 1, n + 1, m - 2, n + 2): #Calling the "check_player2_jumps" to verify the destination grid is eligible for a jump and appending it to the list of available jumps
                        jumpAvail.append([m, n, m - 2, n + 2])
                    if Board.check_player2_jumps(board, m, n, m + 1, n + 1, m + 2, n + 2):
                        jumpAvail.append([m, n, m + 2, n + 2])
        if jump is False:
            jumpAvail.extend(movAvail)
            return jumpAvail
        elif jump is True:
            if len(jumpAvail) == 0:
                return movAvail
            else:
                return jumpAvail

    #Helper method to check piece type in the board grid for Player1 and verify if it is qualified for a jump diagonally
    def check_player2_jumps(board, old_i, old_j, via_i, via_j, new_i, new_j):
        if new_i > 7 or new_i < 0:
            return False
        if new_j > 7 or new_j < 0:
            return False
        if board[via_i][via_j] == "-":
            return False
        if board[via_i][via_j][0] == "X" or board[via_i][via_j][0] == "x":
            return False
        if board[new_i][new_j] != "-":
            return False
        if board[old_i][old_j] == "-":
            return False
        if board[old_i][old_j][0] == "o" or board[old_i][old_j][0] == "O":
            return False
        return True

    #Helper method to check piece type in the board grid for Player2 and verify if it is qualified for a move diagonally
    def check_player2_moves(board, old_i, old_j, new_i, new_j):

        if new_i > 7 or new_i < 0:
            return False
        if new_j > 7 or new_j < 0:
            return False
        if board[old_i][old_j] == "-":
            return False
        if board[new_i][new_j] != "-":
            return False
        if board[old_i][old_j][0] == "o" or board[old_i][old_j][0] == "O": #Indexing the board list to check if the grid is occupied by Player's 1's piece. if it is, returns False
            return False
        if board[new_i][new_j] == "-": #Checks if the grid is free/unoccupied and if it is, returns True to allow player 1 move
            return True


    #Helper method to check moves available for player 1 and store them in a list
    def find_player1_movAvail(board, jump):
        movAvail = [] #List to store available moves for Player 1
        jumpAvail = []# List to store available jump possibilities for Player 1
        for m in range(8):
            for n in range(8):
                if board[m][n][0] == "o": #Checks if the first grid in the board contains the "o" piecetype
                    if Board.check_player1_moves(board, m, n, m - 1, n - 1):
                        movAvail.append([m, n, m - 1, n - 1])
                    if Board.check_player1_moves(board, m, n, m - 1, n + 1):
                        movAvail.append([m, n, m - 1, n + 1])
                    if Board.check_player1_jumps(board, m, n, m - 1, n - 1, m - 2, n - 2):
                        jumpAvail.append([m, n, m - 2, n - 2])
                    if Board.check_player1_jumps(board, m, n, m - 1, n + 1, m - 2, n + 2):
                        jumpAvail.append([m, n, m - 2, n + 2])
                elif board[m][n][0] == "O": #Checks if the first grid in the board contains the "o" piecetype
                    if Board.check_player1_moves(board, m, n, m - 1, n - 1):
                        movAvail.append([m, n, m - 1, n - 1])
                    if Board.check_player1_moves(board, m, n, m - 1, n + 1):
                        movAvail.append([m, n, m - 1, n + 1])
                    if Board.check_player1_jumps(board, m, n, m - 1, n - 1, m - 2, n - 2):
                        jumpAvail.append([m, n, m - 2, n - 2])
                    if Board.check_player1_jumps(board, m, n, m - 1, n + 1, m - 2, n + 2):
                        jumpAvail.append([m, n, m - 2, n + 2])
                    if Board.check_player1_moves(board, m, n, m + 1, n - 1):
                        movAvail.append([m, n, m + 1, n - 1])
                    if Board.check_player1_jumps(board, m, n, m + 1, n - 1, m + 2, n - 2):
                        jumpAvail.append([m, n, m + 2, n - 2])
                    if Board.check_player1_moves(board, m, n, m + 1, n + 1):
                        movAvail.append([m, n, m + 1, n + 1])
                    if Board.check_player1_jumps(board, m, n, m + 1, n + 1, m + 2, n + 2):
                        jumpAvail.append([m, n, m + 2, n + 2])
        if jump is False:
            jumpAvail.extend(movAvail)
            return jumpAvail
        elif jump is True:
            if len(jumpAvail) == 0:
                return movAvail
            else:
                return jumpAvail

    #Helper method to check piece type in the board grid for Player and verify if it is qualified for a move diagonally
    def check_player1_moves(board, old_i, old_j, new_i, new_j):
        if new_i > 7 or new_i < 0:
            return False
        if new_j > 7 or new_j < 0:
            return False
        if board[old_i][old_j] == "-":
            return False
        if board[new_i][new_j] != "-":
            return False
        if board[old_i][old_j][0] == "x" or board[old_i][old_j][0] == "X": #Indexing the board list to check if the grid is occupied by Player's 2 piece. if it is, returns False
            return False
        if board[new_i][new_j] == "-": #Checks if the grid is free/unoccupied and if it is, returns True to allow player 1 move
            return True

    #Helper method to check piece type in the board grid for Player1 and verify if it is qualified for a jump diagonally
    def check_player1_jumps(board, old_i, old_j, via_i, via_j, new_i, new_j):
        if new_i > 7 or new_i < 0:
            return False
        if new_j > 7 or new_j < 0:
            return False
        if board[via_i][via_j] == "-":
            return False
        if board[via_i][via_j][0] == "O" or board[via_i][via_j][0] == "o":
            return False
        if board[new_i][new_j] != "-":
            return False
        if board[old_i][old_j] == "-":
            return False
        if board[old_i][old_j][0] == "x" or board[old_i][old_j][0] == "X": #Indexing the board list to check if the grid is occupied by Player's 2 piece. if it is, returns False
            return False
        return True



    #Helper method that calculate the difference between the grids and allow player to make a move
    def make_a_move(board, old_i, old_j, new_i, new_j, big_letter, kinged_grid):
        letter = board[old_i][old_j][0]
        i_difference = old_i - new_i
        j_difference = old_j - new_j
        if i_difference == -2 and j_difference == 2:
            board[old_i + 1][old_j - 1] = "-"

        elif i_difference == 2 and j_difference == 2:
            board[old_i - 1][old_j - 1] = "-"

        elif i_difference == 2 and j_difference == -2:
            board[old_i - 1][old_j + 1] = "-"

        elif i_difference == -2 and j_difference == -2:
            board[old_i + 1][old_j + 1] = "-"

        if new_i == kinged_grid:
            letter = big_letter
        board[old_i][old_j] = "-"
        board[new_i][new_j] = letter + str(new_i) + str(new_j)

    #This method executes the game and displays the board 
    def play(self):
        print("--------------------------------")
        print(" RENDERING CHECKER BOARD      ")
        print("--------------------------------")


        while True:
            self.printBoard()
            if self.player1_turn is True:
                print("\nPlayer1's turn.") #Prompts player 1 to make a move
                self.get_player1_input()
            else:
                print("Player2's turn." ) #Prompts player 2 to make a move
                self.get_player2_input()
            if self.player1_pieces == 0:
                self.printBoard()
                print("You have no pieces left.\nYOU LOST IN THIS CONTEST!" )
                exit()
            elif self.player2_pieces == 0:
                self.printBoard()
                print("Player2 has no pieces left.\nYOU WIN!" )
                exit()
            elif self.player2_pieces - self.player1_pieces == 7:
                choice = input("You have fewer pieces than your opponent. Do you want end the game?") #Condition to check if one opponent has lesser pieces than the other player
                if choice == "yes":
                    print("You Lost in the Game")
                    exit()
            self.player1_turn = not self.player1_turn
            self.player2_turn = not self.player2_turn
