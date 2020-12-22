import unittest
from tkinter import Scale, Tk
from unittest.mock import MagicMock, patch

from src.frames.crafting_speed_frame import CraftingSpeedFrame
from src.xml_factories.crafting_speed_element import CraftingSpeedElement


class TestRemapWalkFrame(unittest.TestCase):
    master = MagicMock(spec=Tk)
    crafting_speed_element = MagicMock(spec=CraftingSpeedElement)
    crafting_speed_frame = CraftingSpeedFrame(
        crafting_speed_element=crafting_speed_element
    )
    crafting_speed_scale = MagicMock(spec=Scale)
    crafting_speed_frame.crafting_speed_scale = crafting_speed_scale

    def test_it_handles_apply_event(self):
        self.crafting_speed_frame.handle_apply_event(None)
        self.crafting_speed_element.modify.assert_called_once_with(
            self.crafting_speed_scale.get.return_value
        )

    @patch('src.frames.crafting_speed_frame.tk')
    def test_it_loads_current_crafting_speed_on_render(self, tk):
        initial_scale_value = self.crafting_speed_element.get.return_value
        self.crafting_speed_frame.render(master=self.master)
        tk.Scale.return_value.set.assert_called_once_with(initial_scale_value)
