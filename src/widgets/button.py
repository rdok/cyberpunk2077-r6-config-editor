import tkinter as tk

from src.styles import Styles


class Button(tk.Button):
    def __init__(self, **kw):
        super().__init__(
            **kw,
            background=Styles.background(),
            foreground=Styles.foreground(),
            activebackground=Styles.foreground()
        )
