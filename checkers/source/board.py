import numpy as np
from checkers.source import piece

class CheckersGame:
	def __init__(self, board_state, first_player):
		global _board, _cur_player
		_board = board_state
		_cur_player = first_player
		
	@classmethod
	def default_init(cls):
		_init_board = np.empty((8, 8), dtype=object)
		for i in range(8):
			for j in range(8):
				if (((i + j) % 2) == 1):
					if(i <= 2):
						_init_board[i][j] = piece.CheckersPiece(1, 0)
					elif(i >= 5):
						_init_board[i][j] = piece.CheckersPiece(2, 0)
					else:
						_init_board[i][j] = piece.CheckersPiece(0, 0)
				else:
					_init_board[i][j] = piece.CheckersPiece(0, 0)
		return cls(_init_board, 1)

	def board_size(self):
		return _board.shape
		
		
	def val_at_loc(self, x, y):
		return _board[x][y].player_owner
	
	
	def player_turn(self):
		return _cur_player

	
	def move_piece(self, x1, y1, x2, y2):
		global _cur_player
		if((x1 < 0) or (x1 > 7) or (y1 < 0) or (y1 > 7)):
			raise Exception('Invalid location for target piece')
		elif((x2 < 0) or (x2 > 7) or (y2 < 0) or (y2 > 7)):
			raise Exception('Invalid location for piece to move to')
		elif(_board[x1][y1].player_owner == 0):
			raise Exception('There is no piece to move')
		elif((_board[x1][y1].player_owner == 1) and (_cur_player == 1)):
			if(((x2 == (x1 + 1)) or (x2 == (x1 - 1))) and (y2 == y1 + 1)):
				if(_board[x2][y2].player_owner != 0):
					raise Exception('There is another piece occupying the target location')
				else:
					_board[x2][y2].player_owner = 1
					_board[x1][y1].player_owner = 0
					_cur_player = 2
			elif(((x2 == (x1 + 2)) or (x2 == (x1 - 2))) and (y2 == y1 + 2)):
				if(_board[x2][y2].player_owner != 0):
					raise Exception('There is another piece occupying the target location')
				else:
					if((_board[(x1 + x2) // 2][(y1 + y2) // 2].player_owner) != 2):
						raise Exception('There is no enemy piece to jump over!')
					else:
						_board[x2][y2].player_owner = 1
						_board[x1][y1].player_owner = 0
						_board[(x1 + x2) // 2][(y1 + y2) // 2].player_owner = 0
						_cur_player = 2
			else:
				raise Exception('invalid location to move piece')		
		else:
			if(((x2 == (x1 + 1)) or (x2 == (x1 - 1))) and (y2 == y1 - 1)):
				if(_board[x2][y2].player_owner != 0):
					raise Exception('There is another piece occupying the target location')
				else:
					_board[x2][y2].player_owner = 2
					_board[x1][y1].player_owner = 0
					_cur_player = 1
			elif(((x2 == (x1 + 2)) or (x2 == (x1 - 2))) and (y2 == y1 - 2)):
				if(_board[x2][y2].player_owner != 0):
					raise Exception('There is another piece occupying the target location')
				else:
					if(_board[(x1 + x2) // 2][(y1 + y2) // 2].player_owner != 1):
						raise Exception('There is no enemy piece to jump over!')
					else:
						_board[x2][y2].player_owner = 2
						_board[x1][y1].player_owner = 0
						_board[(x1 + x2) // 2][(y1 + y2) // 2].player_owner = 0
						_cur_player = 1
			else:
				raise Exception('invalid location to move piece')	