from argparse import ArgumentParser
from tkinter import Tk

from src.config import Config
from src.frames.crafting_speed_frame import CraftingSpeedFrame
from src.frames.remap_walk_frame import RemapWalkFrame
from src.gui import GUI
from src.transformers.key_transformer import KeyTransformer
from src.xml_editors.IDLocators import IDLocators
from src.xml_editors.crafting_speed_element import CraftingSpeedEditor
from src.xml_editors.walk_key_editor import WalkKeyEditor, XAxis, WalkKey, YAxis


class IOC:
    dependencies: dict = {}

    def __init__(self):
        self.set(ArgumentParser, ArgumentParser())
        self.set(Config, Config())

    def instantiate_dependencies(self):
        self.set(Tk, Tk())
        self.set(KeyTransformer, KeyTransformer())
        self.set(IDLocators, IDLocators())
        self.set(XAxis, XAxis(id_locators=self.get(IDLocators)))
        self.set(YAxis, YAxis(id_locators=self.get(IDLocators)))

        self.set(WalkKey, WalkKey(
            config=self.get(Config),
            transformer=self.get(KeyTransformer),
        ))

        self.set(WalkKeyEditor, WalkKeyEditor(
            config=self.get(Config),
            x_axis=self.get(XAxis),
            y_axis=self.get(YAxis),
            walk_key=self.get(WalkKey)
        ))

        self.set(CraftingSpeedEditor, CraftingSpeedEditor(self.get(Config)))

        self.set(RemapWalkFrame, RemapWalkFrame(
            walk_element=self.get(WalkKeyEditor),
        ))
        self.set(CraftingSpeedFrame, CraftingSpeedFrame(
            element=self.get(CraftingSpeedEditor),
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
