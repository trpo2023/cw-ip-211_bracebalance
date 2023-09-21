import unittest

import main
from main import *


class TestBraceBalance(unittest.TestCase):
    def test_Window(self):
        self.assertEqual(main.root.title(), "Brace Balance")

    def test_Exit(self):
        self.assertRaises(SystemExit)

    def test_DrawWidgets(self):
        self.assertTrue(draw_widgets)


if __name__ == '__main__':
    unittest.main()
