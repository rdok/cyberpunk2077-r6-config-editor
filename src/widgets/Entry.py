import tkinter as tk

from src.Styles import Styles


class Entry(tk.Entry):
    def __init__(self, **kw):
        super().__init__(
            **kw,
            background=Styles.secondary_color(),
            foreground=Styles.font_color(),
            insertbackground=Styles.primary_color(),
            relief=tk.SOLID
        )
