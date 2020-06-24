import numpy as np


# VARIABLES

board = np.array([[" "," "," "],[" "," "," "],[" "," "," "]])

player = ""

switcher_player = {'O':'player', 'X':'machine'}

winner = ""

# FUNCTIONS

# Behaviour of the game at its start
def game_info(player):

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

	while not (player == "O") and not (player == "X"):
		print("Who is starting? Player [O] or Machine [X]?")
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



def player_move(player):
	print("Please enter your move:")
	move = str(input())

	make_move(player, move)

	draw_board()

	return "X"

def machine_move(player):
	print("Machine's move:")

	return "O"


# PLAYING LOOP
player = game_info(player)

print ("Ok, is "+ str(switcher_player.get(player)) + "'s turn:" )

while (winner == ""):
	if player == 'O' : player = player_move(player)
	elif player == 'X' : player = machine_move(player)


