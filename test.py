import unittest

import main
from main import *


class TestBraceBalance(unittest.TestCase):
    def test_Title(self):
        self.assertEqual(main.root.title(), "Brace Balance")

    def test_Exit(self):
        command = 'q'
        if command:
            self.assertRaises(SystemExit)

    def test_Braces(self):
        brace_string = []


if __name__ == '__main__':
    unittest.main()
