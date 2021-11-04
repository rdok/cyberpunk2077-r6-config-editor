from tkinter import Tk

from src.Styles import Styles
from src.Config import Config
from src.frames.DoubleTapDodgeFrame import DoubleTapDodgeFrame
from src.frames.WalkFrame import WalkFrame
from src.frames.hold_actions.CraftingFrame import CraftingFrame
from src.frames.hold_actions.DisassembleFrame import DisassembleFrame
from src.widgets.Frame import Frame


class GUI(Frame):
    master: Tk

    def __init__(self, master: Tk, frames: dict):
        super().__init__(master=master)
        self.frames = frames

    def render_walk_frame(self):
        walk_frame: WalkFrame = self.frames.get(WalkFrame)
        walk_frame.render(master=self.master)

    def render_crafting_frame(self):
        crafting_frame: CraftingFrame = self.frames.get(CraftingFrame)
        crafting_frame.render(master=self.master)

    def render_disassemble_frame(self):
        disassemble_frame: DisassembleFrame = self.frames.get(DisassembleFrame)
        disassemble_frame.render(master=self.master)

    def render_double_tap_dodge_frame(self):
        double_tap_dodge_frame: DoubleTapDodgeFrame = self.frames \
            .get(DoubleTapDodgeFrame)
        double_tap_dodge_frame.render(master=self.master)

    def setup(self, config: Config):
        self.winfo_toplevel().configure(background=Styles.secondary_color())
        self.winfo_toplevel().title(config.app_name())
        self.grid(row=0, column=0)
        self.lift()