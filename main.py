#*********************************************************************************************************#                                                                                       #
#     Name: Stephen Nwagwughiagwu                                                                         #  
#     Description: A python main main module that manages the game and utilizes the methods               # 
#     of the Board Class                                                                                  #
#******************************************************************************************************** #
from Board import Board

def main():

	player1 = input("Enter Player 1's Name: ") #Receiving input for name of the 1st Player
	if player1.isalpha() == False or len(player1) == 0:
		while (True):
			player1 = input("Invalid entry for Player 1's Name - Please Input a Valid Name: ")
			if player1.isalpha() == True and len(player1) > 0:
				break

	player2 = input("Enter Player 2's Name: ") #Receiving input for name of the 2nd Player
	if player2.isalpha() == False or len(player2) == 0: #Validating input for empty string and non-alphabets
		while (True):
			player2 = input("Invalid entry for Player 2's Name - Please Input a Valid Name: ")
			if player2.isalpha() == True and len(player2) > 0:
				break

	beginY_N = input("Begin game play? (Y/N): ") #Request to begin game or quit
	if beginY_N.isalpha() == False:
		while (True):
			print("Invalid entry")
			beginY_N = input("Begin game play? (Y/N): ")
			if beginY_N.isalpha() == True:
				break

	if "Y" == beginY_N.upper():
		boardObj = Board() #Creating an object of the Board class
		boardObj.play() # Calling the play function to execute the game.
	if "N" == beginY_N.upper():
		exit(0)

if __name__ == '__main__':
	main()
    
