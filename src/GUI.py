from tkinter import Tk

from src.Config import Config
from src.Styles import Styles
from src.frames.WalkFrame import WalkFrame
from src.frames.hold_actions.CraftingFrame import CraftingFrame
from src.frames.hold_actions.DisassembleFrame import DisassembleFrame
from src.widgets.frame import Frame


class GUI(Frame):
    crafting_frame: CraftingFrame
    disassemble_frame: DisassembleFrame
    walk_frame: WalkFrame
    master: Tk

    def __init__(
        self,
        master: Tk,
        config: Config,
        walk_frame: WalkFrame,
        crafting_frame: CraftingFrame,
        disassemble_frame: DisassembleFrame,
    ):
        super().__init__(master=master)
        self.winfo_toplevel().configure(background=Styles.secondary_color())
        self.winfo_toplevel().title(config.app_name())
        self.grid(row=0, column=0)
        self.lift()

        self.walk_frame = walk_frame
        self.crafting_frame = crafting_frame
        self.disassemble_frame = disassemble_frame

    def render_walk_frame(self):
        self.walk_frame.render(master=self.master)

    def render_crafting_frame(self):
        self.crafting_frame.render(master=self.master)

    def render_disassemble_frame(self):
        self.disassemble_frame.render(master=self.master)
