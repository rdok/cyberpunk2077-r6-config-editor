import tkinter as tk

from src.Styles import Styles


class Frame(tk.Frame):
    def __init__(self, master=None, **kw):
        kw['bg'] = Styles.secondary_color(),
        kw['pady'] = Styles.pady(),
        kw['padx'] = Styles.padx(),
        tk.Frame.__init__(self, master, **kw)
