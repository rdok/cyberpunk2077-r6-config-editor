import tkinter as tk

from src.styles import Styles


class Label(tk.Label):
    def __init__(self, **kw):
        super().__init__(
            **kw,
            bg=Styles.background(),
            foreground=Styles.foreground()
        )
