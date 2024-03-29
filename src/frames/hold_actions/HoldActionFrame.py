import tkinter as tk
from abc import ABC, abstractmethod

from src.widgets.Button import Button
from src.widgets.ButtonFrame import ButtonFrame
from src.widgets.Frame import Frame
from src.widgets.Label import Label
from src.widgets.Scale import Scale
from src.xml_editors.hold_actions.HoldActionEditor import HoldActionEditor


class HoldActionFrame(ABC):
    hold_action_editor: HoldActionEditor
    scale: Scale
    initial_scale_value = None
    tk: tk
    apply_btn_text = "APPLY"

    def __init__(self, editor: HoldActionEditor):
        self.hold_action_editor = editor

    def render(self, master: tk):
        self.tk = tk
        label_frame = Frame(master=master)
        label_frame.grid(row=self.frame_row(), column=0)
        label = Label(master=label_frame, text=self.label_text())
        label.pack()

        frame = Frame(master=master)
        frame.grid(row=self.frame_row(), column=1)
        scale = Scale(
            master=frame,
            from_=self.from_(),
            to_=self.to_(),
            resolution=self.resolution(),
        )
        initial_scale_value = self.hold_action_editor.get_timeout()
        scale.set(initial_scale_value)
        scale.pack()
        self.scale = scale

        apply_button_frame = ButtonFrame(master=master)
        apply_button_frame.grid(row=self.frame_row(), column=2)
        self.apply_button = Button(master=apply_button_frame, text=self.apply_btn_text)
        self.apply_button.bind("<Button-1>", self.handle_apply_event)
        self.apply_button.bind("<Enter>", self.reset_button_text)
        self.apply_button.pack()

    def reset_button_text(self, event):
        self.apply_button.config(text=self.apply_btn_text)
        self.apply_button.pack()

    def handle_apply_event(self, event):
        scale_value = self.scale.get()
        self.hold_action_editor.set_timeout(scale_value)
        self.apply_button.config(text="Done")
        self.apply_button.pack()

    @abstractmethod
    def label_text(self) -> str:
        pass

    @abstractmethod
    def from_(self) -> float:
        pass

    @abstractmethod
    def to_(self) -> float:
        pass

    @abstractmethod
    def resolution(self) -> float:
        pass

    @abstractmethod
    def frame_row(self) -> int:
        pass
