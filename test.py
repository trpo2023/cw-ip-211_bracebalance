import unittest

from main import *

class TestBraceBalance(unittest.TestCase):
    def test_Exit(self):
        command = 'q'
        if command:
            self.assertRaises(SystemExit)

    def test_UnbalancedBraces(self):
        brace_string = ['d', 'f', 'h', '(']
        self.assertEqual(check_braces(brace_string), 1)
    
    def test_WithoutBraces(self):
        brace_string = []
        self.assertEqual(check_braces(brace_string), -1)

    def test_BalancedBraces(self):
        brace_string = ['i', '{', '(', 'h', ')', '}']
        self.assertEqual(check_braces(brace_string), 0)

    def test_UnbalancedBraces2(self):
        brace_string = ['}', '2', 'f', '(', ')']
        self.assertEqual(check_braces(brace_string), 1)

if __name__ == '__main__':
    unittest.main()
