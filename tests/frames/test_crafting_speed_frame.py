import unittest
from tkinter import Scale, Tk
from unittest.mock import MagicMock, patch

from src.frames.crafting_speed_frame import CraftingSpeedFrame
from src.xml_factories.crafting_speed_element import CraftingSpeedElement


class TestRemapWalkFrame(unittest.TestCase):
    master = MagicMock(spec=Tk)
    element = MagicMock(spec=CraftingSpeedElement)
    frame = CraftingSpeedFrame(element=element)
    scale = MagicMock(spec=Scale)
    frame.crafting_speed_scale = scale

    def test_it_handles_apply_event(self):
        self.frame.handle_apply_event(None)
        timeout = self.scale.get.return_value
        self.element.set_timeout.assert_called_once_with(timeout)

    @patch('src.frames.crafting_speed_frame.Scale')
    @patch('src.frames.crafting_speed_frame.Frame')
    def test_it_loads_current_crafting_speed_timeout(self,  frame, scale):
        master = MagicMock(spec=Tk)
        initial_scale_value = self.element.get_timeout.return_value
        self.frame.render(master=master)
        scale.return_value.set.assert_called_once_with(initial_scale_value)
