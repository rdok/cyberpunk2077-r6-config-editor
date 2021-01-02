import unittest
from unittest.mock import MagicMock

from src.frames.hold_actions.CraftingFrame import CraftingFrame
from src.frames.hold_actions.HoldActionFrame import HoldActionFrame


class TestCraftingFrame(unittest.TestCase):
    crafting_frame: CraftingFrame

    def setUp(self) -> None:
        editor = MagicMock()
        self.crafting_frame = CraftingFrame(editor=editor)

    def test_it_implements_hold_action_frame(self):
        self.assertIsInstance(self.crafting_frame, HoldActionFrame)

    def test_it_maintains_the_label_text(self):
        self.assertEqual('CRAFTING SPEED', self.crafting_frame.label_text())

    def test_it_maintains_the_minimum_timeout_value(self):
        self.assertEqual(0.01, self.crafting_frame.from_())

    def test_it_maintains_the_maximum_timeout_value(self):
        self.assertEqual(1.0, self.crafting_frame.to_())

    def test_it_maintains_the_timeout_increment_value(self):
        self.assertEqual(0.01, self.crafting_frame.resolution())

    def test_it_maintains_the_frame_position(self):
        self.assertEqual(2, self.crafting_frame.frame_row())
