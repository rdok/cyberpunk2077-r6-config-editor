import unittest

from src.styles import Styles

styles = Styles()


class TestStyles(unittest.TestCase):
    def test_it_maintains_the_background(self):
        self.assertEqual('#332a57', styles.background())

    def test_it_maintains_the_foreground(self):
        self.assertEqual('#42a5f5', styles.foreground())

    def test_it_maintains_the_trough(self):
        self.assertEqual('#c0278a', styles.trough())

    def test_it_maintains_the_borderwidth(self):
        self.assertEqual(0, styles.border_width())

    def test_it_maintains_the_pady(self):
        self.assertEqual(20, styles.pady())

    def test_it_maintains_the_padx(self):
        self.assertEqual(20, styles.padx())
