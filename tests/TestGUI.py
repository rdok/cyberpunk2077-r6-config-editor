import unittest
from tkinter import Tk
from unittest.mock import MagicMock

from src.Config import Config
from src.frames.hold_actions.CraftingFrame import CraftingFrame
from src.frames.WalkFrame import WalkFrame
from src.GUI import GUI

master = Tk()
remap_walk_frame = MagicMock(spec=WalkFrame)
crafting_speed_frame = MagicMock(spec=CraftingFrame)
disassemble_speed_frame = MagicMock(spec=CraftingFrame)

gui = GUI(
    master=master,
    config=Config(),
    walk_frame=remap_walk_frame,
    crafting_frame=crafting_speed_frame,
    disassemble_frame=disassemble_speed_frame,
)


class TestGUI(unittest.TestCase):
    def test_it_renders_remap_walk_frame(self):
        gui.render_walk_frame()
        remap_walk_frame.render.assert_called_once_with(master=master)

    def test_it_renders_crafting_speed_frame(self):
        gui.render_crafting_frame()
        crafting_speed_frame.render.assert_called_once_with(master=master)

    def test_it_renders_disassemble_speed_frame(self):
        gui.render_disassemble_frame()
        disassemble_speed_frame.render.assert_called_once_with(master=master)
