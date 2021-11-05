import unittest
from unittest.mock import MagicMock

from src.Config import Config
from src.GUI import GUI
from src.Styles import Styles
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

        frames = {
            WalkFrame: self.walk_frame,
            CraftingFrame: self.crafting_frame,
            DisassembleFrame: self.disassemble_frame,
            DoubleTapDodgeFrame: self.double_tap_dodge_frame
        }

        self.master = MagicMock()
        self.gui = GUI(master=self.master, frames=frames)
        self.gui.winfo_toplevel = MagicMock()
        self.gui.grid = MagicMock()
        self.gui.lift = MagicMock()

    def test_it_configures_styles(self):
        self.gui.setup(MagicMock(spec=Config))
        self.gui.winfo_toplevel().configure \
            .assert_called_once_with(background=Styles.secondary_color())

    def test_it_configures_title(self):
        config = MagicMock(spec=Config)
        self.gui.setup(config)
        self.gui.winfo_toplevel().title \
            .assert_called_once_with(config.app_name())

    def test_it_configures_grid(self):
        self.gui.setup(MagicMock(spec=Config))
        self.gui.grid.assert_called_once_with(row=0, column=0)

    def test_it_configures_lift(self):
        self.gui.setup(MagicMock(spec=Config))
        self.gui.lift.assert_called_once()

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
