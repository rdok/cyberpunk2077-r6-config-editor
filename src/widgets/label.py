import tkinter as tk

from src.Styles import Styles


class Label(tk.Label):
    def __init__(self, **kw):
        super().__init__(
            **kw,
            bg=Styles.secondary_color(),
            foreground=Styles.font_color()
        )
