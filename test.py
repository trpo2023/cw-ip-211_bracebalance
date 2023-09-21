import unittest

import main
from main import *
from tkinter import *


class TestBraceBalance(unittest.TestCase):
    def Window_test(self):
        self.assertEqual(close_program(), SystemExit)
        self.assertEqual(func(5), 6)


if __name__ == '__main__':
    unittest.main()
