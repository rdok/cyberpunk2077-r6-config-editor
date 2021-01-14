import tkinter as tk
from abc import ABC, abstractmethod

from src.widgets.Button import Button
from src.widgets.ButtonFrame import ButtonFrame
from src.widgets.Frame import Frame
from src.widgets.Label import Label
from src.widgets.toggle_frame.ToggleEditor import ToggleEditor


class ToggleFrame(ABC):
    tk: tk

    def __init__(self, toggle_editor: ToggleEditor):
        self.toggle_editor = toggle_editor

    def render(self, master: tk):
        self.tk = tk
        label_frame = Frame(master=master)
        label_frame.grid(row=self.frame_row(), column=0)
        label = Label(master=label_frame, text=self.label_text())
        label.pack()

        enabled = self.toggle_editor.is_enabled()

        state_label_frame = Frame(master=master)
        state_label_frame.grid(row=self.frame_row(), column=1)
        text = self.get_state_txt(enabled)
        self.state_label = Label(master=state_label_frame, text=text)
        self.state_label.pack()

        toggle_button_frame = ButtonFrame(master=master)
        toggle_button_frame.grid(row=self.frame_row(), column=2)

        text = self.get_btn_txt(enabled)
        self.button = Button(master=toggle_button_frame, text=text)
        self.button.bind('<Button-1>', self.handle_button_pressed)
        self.button.bind('<Enter>', self.reset_button_text)
        self.button.pack()

    def reset_button_text(self, event):
        enabled = self.toggle_editor.is_enabled()
        text = self.get_btn_txt(enabled)
        self.button.config(text=text)
        self.button.pack()

    def handle_button_pressed(self, event):
        enabled = self.toggle_editor.is_enabled()

        if enabled:
            self.dispatch_disable_event()
        else:
            self.dispatch_enable_event()

        enabled = self.toggle_editor.is_enabled()
        self.state_label.config(text=self.get_state_txt(enabled))
        self.button.config(text='DONE')
        self.state_label.pack()
        self.button.pack()

    def get_state_txt(self, enabled):
        return 'ENABLED' if enabled is True else 'DISABLED'

    def get_btn_txt(self, enabled):
        return 'DISABLE' if enabled is True else 'ENABLE'

    @abstractmethod
    def label_text(self) -> str:
        pass

    @abstractmethod
    def frame_row(self) -> int:
        pass

    @abstractmethod
    def dispatch_disable_event(self):
        pass

    @abstractmethod
    def dispatch_enable_event(self):
        pass
