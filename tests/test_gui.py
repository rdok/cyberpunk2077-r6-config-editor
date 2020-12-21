import unittest
from tkinter import Tk
from unittest.mock import MagicMock

from src.frames.remap_walk_frame import RemapWalkFrame
from src.gui import GUI
from src.ioc import IOC

ioc = IOC()

remap_walk_frame = MagicMock(spec=RemapWalkFrame)
ioc.set(RemapWalkFrame, remap_walk_frame)


class TestGUI(unittest.TestCase):
    def test_it_creates_remap_walk_frame(self):
        gui = GUI(master=Tk(), remap_walk_frame=remap_walk_frame)
        gui.create_remap_walk_frame()

        remap_walk_frame.render.assert_called_once()