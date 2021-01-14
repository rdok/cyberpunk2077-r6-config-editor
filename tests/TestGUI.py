import unittest
from tkinter import Tk
from unittest.mock import MagicMock

from src.Config import Config
from src.GUI import GUI
from src.frames.DoubleTapDodgeFrame import DoubleTapDodgeFrame
from src.frames.WalkFrame import WalkFrame
from src.frames.hold_actions.CraftingFrame import CraftingFrame
from src.frames.hold_actions.DisassembleFrame import DisassembleFrame


class TestGUI(unittest.TestCase):
    def setUp(self) -> None:
        self.disassemble_frame = MagicMock(spec=DisassembleFrame)
        self.walk_frame = MagicMock(spec=WalkFrame)
        self.crafting_frame = MagicMock(spec=CraftingFrame)
        self.double_tap_dodge_frame = MagicMock(spec=DoubleTapDodgeFrame)

        self.master = Tk()
        frames = {
            WalkFrame: self.walk_frame,
            CraftingFrame: self.crafting_frame,
            DisassembleFrame: self.disassemble_frame,
            DoubleTapDodgeFrame: self.double_tap_dodge_frame
        }

        self.gui = GUI(master=self.master, config=Config(), frames=frames)

    def test_it_renders_walk_frame(self):
        self.gui.render_walk_frame()
        self.walk_frame.render.assert_called_once_with(master=self.master)

    def test_it_renders_crafting_frame(self):
        self.gui.render_crafting_frame()
        self.crafting_frame.render.assert_called_once_with(master=self.master)

    def test_it_renders_disassemble_frame(self):
        self.gui.render_disassemble_frame()
        self.disassemble_frame.render \
            .assert_called_once_with(master=self.master)

    def test_it_renders_double_tap_frame(self):
        self.gui.render_double_tap_dodge_frame()
        self.double_tap_dodge_frame.render \
            .assert_called_once_with(master=self.master)
