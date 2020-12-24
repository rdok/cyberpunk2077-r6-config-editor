import tkinter as tk

from src.styles import Styles


class Scale(tk.Scale):
    def __init__(self, **kw):
        super().__init__(
            **kw,
            background=Styles.secondary_color(),
            foreground=Styles.font_color(),
            activebackground=Styles.foreground_color(),
            troughcolor=Styles.trough_color(),
            highlightbackground=Styles.secondary_color(),
            orient=tk.HORIZONTAL,
            relief=tk.SOLID
        )
