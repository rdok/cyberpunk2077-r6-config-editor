from argparse import ArgumentParser
from tkinter import Tk

from src.Config import Config
from src.GUI import GUI
from src.frames.DoubleTapDodgeFrame import DoubleTapDodgeFrame
from src.frames.WalkFrame import WalkFrame
from src.frames.hold_actions.CraftingFrame import CraftingFrame
from src.frames.hold_actions.DisassembleFrame import DisassembleFrame
from src.transformers.KeyTransformer import KeyTransformer
from src.xml_editors.CustomTreeBuilder import CustomTreeBuilder
from src.xml_editors.DoubleTapDodgeEditor import DoubleTapDodgeEditor
from src.xml_editors.IDLocators import IDLocators
from src.xml_editors.hold_actions.CraftingEditor import CraftingEditor
from src.xml_editors.hold_actions.DisassembleEditor import DisassembleEditor
from src.xml_editors.walk_key_editor import WalkEditor, XAxis, WalkKey, YAxis


class IOC:
    dependencies: dict = {}

    def __init__(self):
        self.set(ArgumentParser, ArgumentParser())
        self.set(Config, Config())

    def instantiate_dependencies(self):
        self.set(Tk, Tk())
        self.set(KeyTransformer, KeyTransformer())
        self.set(IDLocators, IDLocators())
        self.set(CustomTreeBuilder, CustomTreeBuilder())
        self.set(XAxis, XAxis(id_locators=self.get(IDLocators)))
        self.set(YAxis, YAxis(id_locators=self.get(IDLocators)))

        self.set(
            WalkKey,
            WalkKey(
                config=self.get(Config),
                transformer=self.get(KeyTransformer),
                parser=self.get(CustomTreeBuilder),
            ),
        )

        self.set(
            WalkEditor,
            WalkEditor(
                config=self.get(Config),
                x_axis=self.get(XAxis),
                y_axis=self.get(YAxis),
                walk_key=self.get(WalkKey),
                parser=self.get(CustomTreeBuilder),
            ),
        )

        self.set(CraftingEditor, CraftingEditor(config=self.get(Config)))

        self.set(DoubleTapDodgeEditor, DoubleTapDodgeEditor(config=self.get(Config)))

        self.set(DisassembleEditor, DisassembleEditor(config=self.get(Config)))

        self.set(
            WalkFrame,
            WalkFrame(walk_editor=self.get(WalkEditor), walk_key=self.get(WalkKey)),
        )
        self.set(
            CraftingFrame,
            CraftingFrame(
                editor=self.get(CraftingEditor),
            ),
        )

        self.set(
            DisassembleFrame,
            DisassembleFrame(
                editor=self.get(DisassembleEditor),
            ),
        )

        self.set(
            DoubleTapDodgeFrame,
            DoubleTapDodgeFrame(
                toggle_editor=self.get(DoubleTapDodgeEditor),
            ),
        )

        frames = {
            WalkFrame: self.get(WalkFrame),
            CraftingFrame: self.get(CraftingFrame),
            DisassembleFrame: self.get(DisassembleFrame),
            DoubleTapDodgeFrame: self.get(DoubleTapDodgeFrame),
        }

        gui = GUI(master=self.get(Tk), frames=frames)
        gui.setup(config=self.get(Config))
        self.set(GUI, gui)

    def has(self, class_reference):
        return class_reference in self.dependencies

    def new(self, class_reference):
        dependency = self.dependencies.get(class_reference)
        return dependency()

    def get(self, class_reference):
        dependency = self.dependencies.get(class_reference)

        if dependency is None:
            raise Exception(f"Dependency {class_reference} not found")

        return dependency

    def set(self, class_reference, object):
        self.dependencies[class_reference] = object
