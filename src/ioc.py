from argparse import ArgumentParser
from tkinter import Tk

from src.config import Config
from src.framers.slow_walk_creator import SlowWalkCreator
from src.services.element_appender import ElementAppender


class IOC:
    def __init__(self):
        config = Config()

        self.dependencies = {
            ElementAppender: ElementAppender(),
            ArgumentParser: ArgumentParser(),
            Tk: Tk(),
            Config: Config(),
            SlowWalkCreator: SlowWalkCreator(config)
        }

    def has(self, class_reference):
        return class_reference in self.dependencies

    def get(self, class_reference):
        return self.dependencies.get(class_reference)

    def set(self, class_reference, object):
        self.dependencies[class_reference] = object
