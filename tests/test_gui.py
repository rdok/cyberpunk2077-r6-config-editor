import unittest
from tkinter import Tk
from unittest.mock import MagicMock

from src.config import Config
from src.frames.crafting_speed_frame import CraftingSpeedFrame
from src.frames.remap_walk_frame import RemapWalkFrame
from src.gui import GUI

master = Tk()
remap_walk_frame = MagicMock(spec=RemapWalkFrame)
crafting_speed_frame = MagicMock(spec=CraftingSpeedFrame)

gui = GUI(
    master=master,
    config=Config(),
    remap_walk_frame=remap_walk_frame,
    crafting_speed_frame=crafting_speed_frame
)


class TestGUI(unittest.TestCase):
    def test_it_creates_remap_walk_frame(self):
        gui.create_remap_walk_frame()
        remap_walk_frame.render.assert_called_once_with(master=master)

    def test_it_creates_crafting_speed_frame(self):
        gui.create_crafting_speed_frame()
        crafting_speed_frame.render.assert_called_once_with(master=master)
