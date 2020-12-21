import tkinter as tk
from tkinter import Tk

from src.config import Config
from src.frames.remap_walk_frame import RemapWalkFrame


class GUI(tk.Frame):
    remap_walk_frame: RemapWalkFrame
    master: Tk

    def __init__(
        self, master: Tk, remap_walk_frame: RemapWalkFrame, config: Config
    ):
        super().__init__(master)

        self.winfo_toplevel().title(config.app_name())

        self.grid(row=0, column=0, padx=20, pady=20)
        self.lift()
        self.remap_walk_frame = remap_walk_frame

    def create_remap_walk_frame(self):
        self.remap_walk_frame.render(master=self.master)
