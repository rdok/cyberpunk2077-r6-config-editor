import unittest
from unittest.mock import MagicMock

from src.frames.DoubleTapDodgeFrame import DoubleTapDodgeFrame


class TestDoubleTapDodgeFrame(unittest.TestCase):
    frame: DoubleTapDodgeFrame

    def setUp(self) -> None:
        editor = MagicMock()
        self.frame = DoubleTapDodgeFrame()

    def test_it_maintains_the_label_text(self):
        self.assertEqual('DOUBLE TAP DODGE', self.frame.label_text())

    # todo: move this to double tap dodge
    # def test_it_maintains_the_default_count_value(self):
    #     self.assertEqual(2, self.frame.default_count())

    # def test_it_maintains_the_frame_position(self):
    #     self.assertEqual(4, self.frame.frame_row())
