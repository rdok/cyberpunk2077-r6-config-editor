import tkinter as tk

from src.styles import Styles


class Button(tk.Button):
    def __init__(self, **kw):
        super().__init__(
            **kw,
            activebackground=Styles.primary_color(),
            activeforeground=Styles.primary_color(),
            borderwidth=Styles.border_width(),
            foreground=Styles.font_color(),
            background=Styles.secondary_color(),
            highlightthickness=Styles.btn_highlightthickness(),
            relief=tk.SOLID,
            width=Styles.button_width(),
        )
