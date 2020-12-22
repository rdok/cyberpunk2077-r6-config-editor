from argparse import ArgumentParser
from tkinter import Tk

from src.config import Config
from src.frames.crafting_speed_frame import CraftingSpeedFrame
from src.frames.remap_walk_frame import RemapWalkFrame
from src.gui import GUI
from src.transformers.key_transformer import KeyTransformer
from src.xml_factories.button_factory import ButtonFactory
from src.xml_factories.crafting_speed_element import CraftingSpeedElement


class IOC:
    dependencies: dict = {}

    def __init__(self):
        self.set(Tk, Tk())
        self.set(Config, Config())
        self.set(ArgumentParser, ArgumentParser())
        self.set(KeyTransformer, KeyTransformer())
        self.set(CraftingSpeedElement, CraftingSpeedElement())

        self.set(ButtonFactory, ButtonFactory(
            key_transformer=self.get(KeyTransformer),
            config=self.get(Config)
        ))

        self.set(RemapWalkFrame, RemapWalkFrame(
            button_factory=self.get(ButtonFactory),
        ))
        self.set(CraftingSpeedFrame, CraftingSpeedFrame(
            crafting_speed_element=self.get(CraftingSpeedElement),
        ))

        self.set(GUI, GUI(
            master=self.get(Tk),
            config=self.get(Config),
            remap_walk_frame=self.get(RemapWalkFrame),
            crafting_speed_frame=self.get(CraftingSpeedFrame)
        ))

    def has(self, class_reference):
        return class_reference in self.dependencies

    def get(self, class_reference):
        dependency = self.dependencies.get(class_reference)

        if dependency is None:
            raise Exception(f'Dependency {class_reference} not found')

        return dependency

    def set(self, class_reference, object):
        self.dependencies[class_reference] = object
