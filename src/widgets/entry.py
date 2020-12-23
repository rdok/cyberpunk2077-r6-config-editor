import tkinter as tk

from src.styles import Styles


class Entry(tk.Entry):
    def __init__(self, **kw):
        super().__init__(
            **kw,
            background=Styles.background(),
            foreground=Styles.foreground()
        )
