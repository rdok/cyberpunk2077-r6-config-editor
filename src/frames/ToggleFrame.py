import tkinter as tk
from abc import ABC, abstractmethod

from src.widgets.button import Button
from src.widgets.button_frame import ButtonFrame
from src.widgets.frame import Frame
from src.widgets.label import Label


class ToggleFrame(ABC):
    tk: tk

    def render(self, master: tk):
        self.tk = tk
        label_frame = Frame(master=master)
        label_frame.grid(row=self.frame_row(), column=0)
        label = Label(master=label_frame, text=self.label_text())
        label.pack()

        frame = Frame(master=master)
        frame.grid(row=self.frame_row(), column=1)

        apply_button_frame = ButtonFrame(master=master)
        apply_button_frame.grid(row=self.frame_row(), column=2)
        apply_button = Button(master=apply_button_frame, text="APPLY")
        apply_button.bind('<Button-1>', self.handle_apply_event)
        apply_button.pack()

    def handle_apply_event(self, event):
        pass

    @abstractmethod
    def label_text(self) -> str:
        pass

    @abstractmethod
    def frame_row(self) -> int:
        pass
