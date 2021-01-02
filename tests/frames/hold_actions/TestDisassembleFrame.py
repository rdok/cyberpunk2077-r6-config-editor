import unittest
from unittest.mock import MagicMock

from src.frames.hold_actions.DisassembleFrame import DisassembleFrame
from src.frames.hold_actions.HoldActionFrame import HoldActionFrame


class TestDisassembleFrame(unittest.TestCase):
    frame: DisassembleFrame

    def setUp(self) -> None:
        editor = MagicMock()
        self.frame = DisassembleFrame(editor=editor)

    def test_it_implements_hold_action_frame(self):
        self.assertIsInstance(self.frame, HoldActionFrame)

    def test_it_maintains_the_label_text(self):
        self.assertEqual('DISASSEMBLE SPEED', self.frame.label_text())

    def test_it_maintains_the_minimum_timeout_value(self):
        self.assertEqual(0.01, self.frame.from_())

    def test_it_maintains_the_maximum_timeout_value(self):
        self.assertEqual(1.0, self.frame.to_())

    def test_it_maintains_the_timeout_increment_value(self):
        self.assertEqual(0.01, self.frame.resolution())

    def test_it_maintains_the_frame_position(self):
        self.assertEqual(3, self.frame.frame_row())
