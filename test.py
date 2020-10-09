from foo import afunction

import unittest

class TestSum(unittest.TestCase):
    def test_function1(self):
        """
        Test that it can sum a list of integers
        """
        result = afunction(1)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

