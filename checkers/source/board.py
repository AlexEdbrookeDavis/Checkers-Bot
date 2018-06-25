import numpy as np

def initilize():
	global board
	board = np.zeros((10, 10))
	for i in range(10):
		for j in range(10):
			if (((i + j) % 2) == 1):
				board[i][j] = 1

	
def board_size():
    return board.shape
	
def val_at_loc(i, j):
    return board[i][j]