import unittest
from unittest.mock import patch

from input import main

class GetInputTest(unittest.TestCase):

    @patch('builtins.input', return_value="yes")
    def test_output(self,m):
        
        dct = []
        self.ans = main()
        for value in self.ans:
            dct.append(value)
        self.assertEqual("yes",dct[0])
        self.assertEqual("no",dct[1])
        self.assertEqual("fail",dct[2])


if __name__ == "__main__":
    unittest.main()