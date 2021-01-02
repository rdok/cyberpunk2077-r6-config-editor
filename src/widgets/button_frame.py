import tkinter as tk

from src.Styles import Styles


class ButtonFrame(tk.Frame):
    def __init__(self, master=None, **kw):
        kw['highlightbackground'] = Styles.primary_color(),
        kw['highlightcolor'] = Styles.primary_color(),
        kw['highlightthickness'] = 2,
        kw['pady'] = 0,
        kw['padx'] = 0,

        tk.Frame.__init__(self, master, **kw)
