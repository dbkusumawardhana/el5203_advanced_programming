import unittest
import numpy as np
from bubble_sort import bubble_sort

class SortTestCase(unittest.TestCase):

	def test_bubble_sort(self):
		input_testing =  [0, 3, 1, 7, 5, 8, 2, 9, 6, 4]
		expected_result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		result = bubble_sort(input_testing)
		self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()