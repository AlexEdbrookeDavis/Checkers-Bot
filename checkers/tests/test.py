import unittest
from checkers.source import board

class MyFirstTests(unittest.TestCase):
	
	def test_board_size(self):
		board.initilize()
		self.assertEqual(board.board_size(), (10, 10))
		
	def test_board_init_state(self):
		board.initilize()
		for i in range(10):
			for j in range(10):
				if (((i + j) % 2) == 1):
					self.assertEqual(board.val_at_loc(i, j), 1)
				else:
					self.assertEqual(board.val_at_loc(i, j), 0)		
					
					
if __name__ == '__main__':
    unittest.main()  