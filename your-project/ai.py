import numpy as np
import generate_oportunities


#-----------------------------------
# VARIABLES
#-----------------------------------

corners = ['ul', 'ur', 'bl', 'br']


possibility_player = []
possibility_machine = []

oportunity_player = []
oportunity_machine = []

'''
 RULES

 1. Winning
 2. Not losing
 3. Win center
 4. Double possibility
 5. Corner possibility
 6. Possibility
 7. Corner available
 8. Free cell

'''

#-----------------------------------
# FUNCTIONS
#-----------------------------------


def choose_cell(board):
	possibility_machine, possibility_player = generate_oportunities.generate_oportunities(board)

	#1. Winning
	if len(possibility_machine) > 0 : return possibility_machine.pop()

	#2. Not Losing
	elif len(possibility_player) > 0 : return possibility_player.pop()

	#3. Cover Center
	elif board[1,1] == " " : return 'cm'


	#4. Double possibility



	#5. Corner possibility



	#6. Possibility



	#7. Corner available
	# No special order, just the 4 of them
	elif (board[0,0] == " ") : return 'ul'
	elif (board[0,2] == " ") : return 'ur'
	elif (board[2,0] == " ") : return 'bl'
	elif (board[2,2] == " ") : return 'br'


	#8. Free cell
	# Again, no special order, just the 4 left
	elif (board[0,1] == " ") : return 'um'
	elif (board[1,0] == " ") : return 'cl'
	elif (board[1,2] == " ") : return 'cr'
	elif (board[2,1] == " ") : return 'bm'

