from argparse import ArgumentParser
from tkinter import Tk

from src.config import Config
from src.frames.slow_walk_frame import RemapWalkFrame
from src.gui import GUI
from src.services.element_appender import ElementAppender


class IOC:
    dependencies: dict = {}

    def __init__(self):
        remap_walk_frame = RemapWalkFrame(element_appender=ElementAppender())
        self.set(RemapWalkFrame, remap_walk_frame)

        window = Tk()
        self.set(Tk, window)

        gui = GUI(master=window, remap_walk_frame=remap_walk_frame)
        self.set(GUI, gui)

        self.set(Config, Config())
        self.set(ArgumentParser, ArgumentParser())
        self.set(ElementAppender, ElementAppender())

    def has(self, class_reference):
        return class_reference in self.dependencies

    def get(self, class_reference):
        dependency = self.dependencies.get(class_reference)

        if dependency is None:
            raise Exception(f'Dependency {class_reference} not found')

        return dependency

    def set(self, class_reference, object):
        self.dependencies[class_reference] = object
