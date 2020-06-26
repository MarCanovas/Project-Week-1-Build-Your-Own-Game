import numpy as np
import ai

#-----------------------------------
# VARIABLES
#-----------------------------------


# This contains the board with the values to be printed
# It also contains the occupied cells to check for options
board = np.array([[" "," "," "],[" "," "," "],[" "," "," "]])

# Player saves the current turn
# It can be "X" or "O"
player = ""

# Relates tokens with the name of the players
switcher_player = {'O':'player', 'X':'machine'}

# Relates names of moves with their board positions
move_translate = {
	'ul' : (0,0),	'lu' : (0,0),
	'um' : (0,1),	'mu' : (0,1),
	'ur' : (0,2),	'ru' : (0,2),

	'cl' : (1,0),	'lc' : (1,0),
	'cm' : (1,1),	'mc' : (1,1),
	'cr' : (1,2),	'rc' : (1,2),

	'bl' : (2,0),	'lb' : (2,0),
	'bm' : (2,1),	'mb' : (2,1),
	'br' : (2,2),	'rb' : (2,2)
}

# Stores the winner of the game if there is one
winner = ""

#-----------------------------------
# FUNCTIONS
#-----------------------------------


# Behaviour of the game at its start
# Most of them are prints to explain the game
# PARAMS: NONE
# RETURN: The player who will have the first turn
def game_info():

	print("      -----------------------------")
	print("      |  Welcome to TIC TAC TOE!  |")
	print("      -----------------------------")

	print()

	print("This is the BOARD we are going to use.")

	print()

	print("In order to select a cell we will combine 1st letter of the directions.")
	print("For example, 'left + up' will be referred as the cell 'lu' or 'ul'")

	print()

	draw_board()

	print()

	player = ""
	
	while not (player == "O") and not (player == "X"):
		print("Who is starting? Player [O] or Machine [X]?")
		player = input();

	return player


# Prints the board in its current state
# PARAMS: NONE
# RETURN: NONE
def draw_board():
	print("          left   middle   right   ")
	print("         -----------------------")
	print(" up     |   "+ board[0,0] +"   |   "+ board[0,1] +"   |   "+ board[0,2] +"   |")
	print("         -----------------------")
	print("center  |   "+ board[1,0] +"   |   "+ board[1,1] +"   |   "+ board[1,2] +"   |")
	print("         -----------------------")
	print("bottom  |   "+ board[2,0] +"   |   "+ board[2,1] +"   |   "+ board[2,2] +"   |")
	print("         -----------------------")


#-----------------------------------

# 'Draws' the token on the board for the player that calls it
# PARAMS: The player who makes the move
# PARAMS: The move that player makes
# RETURN: NONE
def make_move(player, move):
	if (move == 'ul') or (move == 'lu') : board[0,0] = player
	elif (move == 'um') or (move == 'mu') : board[0,1] = player
	elif (move == 'ur') or (move == 'ru') : board[0,2] = player

	elif (move == 'cl') or (move == 'lc') : board[1,0] = player
	elif (move == 'cm') or (move == 'mc') : board[1,1] = player
	elif (move == 'cr') or (move == 'rc') : board[1,2] = player

	elif (move == 'bl') or (move == 'lb') : board[2,0] = player
	elif (move == 'bm') or (move == 'mb') : board[2,1] = player
	elif (move == 'br') or (move == 'rb') : board[2,2] = player


# Check if the move is correct and refers to a free cell
# PARAMS: The move to check
# RETURN: NONE
def check_not_valid_move(move):
	if not move in move_translate.keys() : return 1
	m = move_translate[move]

	if board[m[0],m[1]] != " " : return 1
	else: return 0

# Interacts with the player and call all the functions to make its move
# PARAMS: The player whose turn is
# RETURN: The next player to play
def player_move(player):
	print("Please enter your move:")
	move = str(input())

	while check_not_valid_move(move):
		print("Not valid move, choose another:")
		move = str(input())

	make_move(player, move)

	draw_board()

	return "X"

# Calls the ai module methods to choose a cell
# PARAMS: The player whose turn is
# RETURN: The next player to play
def machine_move(player):
	move = ai.choose_cell(board)
	make_move(player, move)

	print("Machine's move:")
	draw_board()

	return "O"




#-----------------------------------

# Check if there are three of the same tokens aligned
# PARAMS: NONE
# RETURN: The player who won, if there is one
def check_winner():
	winner = ""

	#ROWS
	if (board[0,0] == board[0,1]) and (board[0,0] == board[0,2]) and (not board[0,0] == " "):
		winner = board[0,0]
	if (board[1,0] == board[1,1]) and (board[1,0] == board[1,2]) and (not board[1,0] == " "):
		winner = board[1,0]
	if (board[2,0] == board[2,1]) and (board[2,0] == board[2,2]) and (not board[2,0] == " "):
		winner = board[2,0]
	
	#COLUMNS
	if (board[0,0] == board[1,0]) and (board[0,0] == board[2,0]) and (not board[0,0] == " "):
		winner = board[0,0]
	if (board[0,1] == board[1,1]) and (board[0,1] == board[2,1]) and (not board[0,1] == " "):
		winner = board[0,1]
	if (board[0,2] == board[1,2]) and (board[0,2] == board[2,2]) and (not board[0,2] == " "):
		winner = board[0,2]

	#DIAGONALS
	if (board[0,0] == board[1,1]) and (board[0,0] == board[2,2]) and (not board[0,0] == " "):
		winner = board[0,0]
	if (board[0,2] == board[1,1]) and (board[0,2] == board[2,0]) and (not board[0,2] == " "):
		winner = board[0,2]

	return winner

#-----------------------------------

# Check if there are free cells to keep playing
# PARAMS: NONE 
# RETURN: 1 if there is a free cell, else 0
def check_not_full():
	if " " in board: return 1
	else: return 0

#-----------------------------------
# PLAYING LOOP
#-----------------------------------

# Starts with the game info, getting the first turn
player = game_info()

# Short message to confirm the first player
print ("Ok, is "+ str(switcher_player.get(player)) + "'s turn:" )

# Loop of the game
while (winner == "") and check_not_full():

	# Calls the right move function depending on the turn
	if player == 'O' : player = player_move(player)
	elif player == 'X' : player = machine_move(player)
	
	# Looks for a winner
	winner = check_winner()
	
# If we get out of the loop without a winner
if (winner == ""): print("There is a tie!")
# If someone won
else: print ("The winner is "+ switcher_player[winner] +". Congratulations!")

