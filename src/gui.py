import tkinter as tk
from tkinter import Tk

from src.framers.slow_walk_creator import SlowWalkCreator
from src.ioc import IOC


class GUI(tk.Frame):
    args: object
    ioc: IOC

    def __init__(self, ioc, args):
        window = ioc.get(Tk)
        super().__init__(window)

        self.args = args
        self.ioc = ioc

    def create_slow_walk_mapper(self):
        slow_walk_creator = self.ioc.get(SlowWalkCreator)
        slow_walk_creator.create()
