import unittest
from checkers.source import board
import numpy as np

class MyFirstTests(unittest.TestCase):
	
	def test_board_size(self):
		game = board.CheckersGame.default_init()
		self.assertEqual(game.board_size(), (8, 8))
		
	def test_board_default_state(self):
		game = board.CheckersGame.default_init()
		for i in range(3):
			for j in range(8):
				if (((i + j) % 2) == 1):
					self.assertEqual(game.val_at_loc(i, j), 1)

		for i in range(3):
			for j in range(8):
				if (((i + 5 + j) % 2) == 1):
					self.assertEqual(game.val_at_loc(i + 5, j), 2)		
		self.assertEqual(game.player_turn(), 1)

		
	def test_out_of_board_moves(self):
		game = board.CheckersGame.default_init()
		self.assertRaises(Exception, game.move_piece, 0, 1, -1, 2)
		self.assertRaises(Exception, game.move_piece, -1, -1, 0, 0)

	def test_missing_piece_move(self):
		game = board.CheckersGame.default_init()
		self.assertRaises(Exception, game.move_piece, 0, 0, 1, 1)

	def test_move_collide(self):
		game_state = np.zeros((8, 8))
		game_state[0][1] = 1
		game_state[1][2] = 1
		game = board.CheckersGame(game_state, 1)
		self.assertRaises(Exception, game.move_piece, 0, 1, 1, 2)

	def test_legal_board_move(self):
		game = board.CheckersGame.default_init()
		game.move_piece(2, 1, 3, 2)
		self.assertEqual(game.val_at_loc(2, 1), 0)
		self.assertEqual(game.val_at_loc(3, 2), 1)
		self.assertEqual(game.player_turn(), 2)
		
	def test_legal_jump_move(self):
		game_state = np.zeros((8, 8))
		game_state[0][1] = 1
		game_state[1][2] = 2
		game = board.CheckersGame(game_state, 1)
		game.move_piece(0, 1, 2, 3)
		self.assertEqual(game.val_at_loc(0, 1), 0)
		self.assertEqual(game.val_at_loc(1, 2), 0)
		self.assertEqual(game.val_at_loc(2, 3), 1)
		self.assertEqual(game.player_turn(), 2)

	def test_jump_collide(self):
		game_state = np.zeros((8, 8))
		game_state[0][1] = 1
		game_state[1][2] = 2
		game_state[2][3] = 1
		game = board.CheckersGame(game_state, 1)
		self.assertRaises(Exception, game.move_piece, 0, 1, 2, 3)

	def test_jump_over_invalid(self):
		game_state = np.zeros((8, 8))
		game_state[0][1] = 1
		game_state[1][2] = 1
		game = board.CheckersGame(game_state, 1)
		self.assertRaises(Exception, game.move_piece, 0, 1, 2, 3)

	def test_move_location_invalid(self):
		game_state = np.zeros((8, 8))
		game_state[0][1] = 1
		game = board.CheckersGame(game_state, 1)
		self.assertRaises(Exception, game.move_piece, 0, 1, 1, 1)	
	
	def test_move_collide_reverse(self):
		game_state = np.zeros((8, 8))
		game_state[0][1] = 2
		game_state[1][2] = 2
		game = board.CheckersGame(game_state, 2)
		self.assertRaises(Exception, game.move_piece, 1, 2, 0, 1)

	def test_legal_board_move_reverse(self):
		game_state = np.zeros((8, 8))
		game_state[0][1] = 0
		game_state[1][2] = 2
		game = board.CheckersGame(game_state, 2)
		game.move_piece(1, 2, 0, 1)
		self.assertEqual(game.val_at_loc(1, 2), 0)
		self.assertEqual(game.val_at_loc(0, 1), 2)
		self.assertEqual(game.player_turn(), 1)
		
	def test_legal_jump_move_reverse(self):
		game_state = np.zeros((8, 8))
		game_state[1][2] = 1
		game_state[2][3] = 2
		game = board.CheckersGame(game_state, 2)
		game.move_piece(2, 3, 0, 1)
		self.assertEqual(game.val_at_loc(0, 1), 2)
		self.assertEqual(game.val_at_loc(1, 2), 0)
		self.assertEqual(game.val_at_loc(2, 3), 0)
		self.assertEqual(game.player_turn(), 1)

	def test_jump_collide_reverse(self):
		game_state = np.zeros((8, 8))
		game_state[0][1] = 2
		game_state[1][2] = 1
		game_state[2][3] = 2
		game = board.CheckersGame(game_state, 2)
		self.assertRaises(Exception, game.move_piece, 2, 3, 0, 1)

	def test_jump_over_invalid_reverse(self):
		game_state = np.zeros((8, 8))
		game_state[1][2] = 2
		game_state[2][3] = 2
		game = board.CheckersGame(game_state, 2)
		self.assertRaises(Exception, game.move_piece, 2, 3, 0, 1)

	def test_move_location_invalid_reverse(self):
		game_state = np.zeros((8, 8))
		game_state[0][1] = 2
		game = board.CheckersGame(game_state, 2)
		self.assertRaises(Exception, game.move_piece, 0, 1, 1, 1)		
if __name__ == '__main__':
    unittest.main()  