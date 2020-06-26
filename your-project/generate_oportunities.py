import numpy as np

#-----------------------------------
# FUNCTIONS
#-----------------------------------


def generate_oportunities(board):
	oportunity_player = []
	oportunity_machine = []

	#UL
	if (board[0,0] == " "):
		#ROW
		if (board[0,1] == board[0,2]) and (not board[0,1] == " "):
			if (board[0,1] == "X") : oportunity_machine.append('ul')
			else : oportunity_player.append('ul') 
		#COLUMN
		if (board[1,0] == board[2,0]) and (not board[1,0] == " "):
			if (board[1,0] == "X") : oportunity_machine.append('ul')
			else : oportunity_player.append('ul') 
		#DIAGONAL
		if (board[1,1] == board[2,2]) and (not board[2,2] == " "):
			if (board[1,1] == "X") : oportunity_machine.append('ul')
			else : oportunity_player.append('ul') 
	
	#UM
	if (board[0,1] == " "):
		#ROW
		if (board[0,0] == board[0,2]) and (not board[0,0] == " "):
			if (board[0,0] == "X") : oportunity_machine.append('um')
			else : oportunity_player.append('um') 
		#COLUMN
		if (board[1,1] == board[2,1]) and (not board[1,1] == " "):
			if (board[1,1] == "X") : oportunity_machine.append('um')
			else : oportunity_player.append('um') 


	#UR
	if (board[0,2] == " "):
		#ROW
		if (board[0,1] == board[0,0]) and (not board[0,1] == " "):
			if (board[0,1] == "X") : oportunity_machine.append('ur')
			else : oportunity_player.append('ur') 
		#COLUMN
		if (board[1,2] == board[2,2]) and (not board[1,2] == " "):
			if (board[1,2] == "X") : oportunity_machine.append('ur')
			else : oportunity_player.append('ur') 
		#DIAGONAL
		if (board[1,1] == board[2,0]) and (not board[2,0] == " "):
			if (board[1,1] == "X") : oportunity_machine.append('ur')
			else : oportunity_player.append('ur') 


	#LC
	if (board[1,0] == " "):
		#ROW
		if (board[1,1] == board[1,2]) and (not board[1,1] == " "):
			if (board[1,1] == "X") : oportunity_machine.append('lc')
			else : oportunity_player.append('lc') 
		#COLUMN
		#THIS FAILS
		if (board[0,0] == board[0,2]) and (not board[0,0] == " "):
			if (board[0,0] == "X") : oportunity_machine.append('lc')
			elif  (board[0,0] == "O"): oportunity_player.append('lc') 


	#MC
	if (board[1,1] == " "):
		#ROW
		if (board[1,0] == board[1,2]) and (not board[1,0] == " "):
			if (board[1,0] == "X") : oportunity_machine.append('cm')
			else : oportunity_player.append('cm') 
		#COLUMN
		if (board[0,1] == board[2,1]) and (not board[0,1] == " "):
			if (board[0,1] == "X") : oportunity_machine.append('cm')
			else : oportunity_player.append('cm') 
		#DIAGONAL
		if (board[0,0] == board[2,2]) and (not board[2,2] == " "):
			if (board[2,2] == "X") : oportunity_machine.append('cm')
			else : oportunity_player.append('cm') 
		#DIAGONAL
		if (board[0,2] == board[2,0]) and (not board[2,0] == " "):
			if (board[0,2] == "X") : oportunity_machine.append('cm')
			else : oportunity_player.append('cm') 

	#RC
	if (board[1,2] == " "):
		#ROW
		if (board[1,0] == board[1,1]) and (not board[1,0] == " "):
			if (board[1,0] == "X") : oportunity_machine.append('rc')
			else : oportunity_player.append('rc') 
		#COLUMN
		if (board[0,2] == board[2,2]) and (not board[2,2] == " "):
			if (board[2,2] == "X") : oportunity_machine.append('rc')
			else : oportunity_player.append('rc') 


	#BL
	if (board[2,0] == " "):
		#ROW
		if (board[2,1] == board[2,2]) and (not board[2,1] == " "):
			if (board[2,1] == "X") : oportunity_machine.append('bl')
			else : oportunity_player.append('bl') 
		#COLUMN
		if (board[1,0] == board[0,0]) and (not board[1,0] == " "):
			if (board[1,0] == "X") : oportunity_machine.append('bl')
			else : oportunity_player.append('bl') 
		#DIAGONAL
		if (board[1,1] == board[0,2]) and (not board[0,2] == " "):
			if (board[1,1] == "X") : oportunity_machine.append('bl')
			else : oportunity_player.append('bl') 
	
	#BM
	if (board[2,1] == " "):
		#ROW
		if (board[2,0] == board[2,2]) and (not board[2,0] == " "):
			if (board[2,0] == "X") : oportunity_machine.append('bm')
			else : oportunity_player.append('bm') 
		#COLUMN
		if (board[1,1] == board[0,1]) and (not board[1,1] == " "):
			if (board[1,1] == "X") : oportunity_machine.append('bm')
			else : oportunity_player.append('bm') 


	#BR
	if (board[2,2] == " "):
		#ROW
		if (board[2,1] == board[2,0]) and (not board[2,1] == " "):
			if (board[2,1] == "X") : oportunity_machine.append('ur')
			else : oportunity_player.append('ur') 
		#COLUMN
		if (board[1,2] == board[0,2]) and (not board[1,2] == " "):
			if (board[1,2] == "X") : oportunity_machine.append('ur')
			else : oportunity_player.append('ur') 
		#DIAGONAL
		if (board[1,1] == board[0,0]) and (not board[0,0] == " "):
			if (board[1,1] == "X") : oportunity_machine.append('ur')
			else : oportunity_player.append('ur') 

	return oportunity_machine, oportunity_player
