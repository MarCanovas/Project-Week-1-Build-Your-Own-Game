import numpy as np

#-----------------------------------
# VARIABLES
#-----------------------------------

board = np.array([[" "," "," "],[" "," "," "],[" "," "," "]])

player = ""

switcher_player = {'O':'Player1', 'X':'Player2'}

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

winner = ""

#-----------------------------------
# FUNCTIONS
#-----------------------------------


# Behaviour of the game at its start
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
		print("Who is starting? Player1 [O] or Player2 [X]?")
		player = input();

	return player


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


def make_move(player, move):
	m = move_translate[move]
	board[m[0],m[1]] = player

	if player == "X": return "O"
	elif player == "O": return "X"


def check_not_valid_move(move):
	m = move_translate[move]
	if board[m[0],m[1]] != " " : return 1
	else: return 0



def player_move(player):
	print("Please enter your move:")
	move = str(input())

	while check_not_valid_move(move):
		print("Occupied cell, choose one free:")
		move = str(input())

	make_move(player, move)

	draw_board()

	if player == "O" : return "X"
	elif player == "X" : return "O"


#-----------------------------------


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
# PLAYING LOOP
#-----------------------------------

player = game_info()

print ("Ok, is "+ str(switcher_player.get(player)) + "'s turn:" )

while (winner == ""):
	player = player_move(player)
	winner = check_winner()
	
print ("The winner is "+ winner +". Congratulations!")

