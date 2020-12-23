import tkinter as tk

from src.styles import Styles


class Frame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(
            self,
            master,
            bg=Styles.background(),
            pady=Styles.pady(),
            padx=Styles.padx()
        )
