import tkinter as tk

from src.styles import Styles


class Scale(tk.Scale):
    def __init__(self, **kw):
        super().__init__(
            **kw,
            bg=Styles.background(),
            foreground=Styles.foreground(),
            activebackground=Styles.foreground(),
            troughcolor=Styles.trough(),
            borderwidth=Styles.border_width(),
            highlightbackground=Styles.foreground(),
            orient=tk.HORIZONTAL
        )
