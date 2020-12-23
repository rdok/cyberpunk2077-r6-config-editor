import tkinter as tk
from tkinter import Scale

from src.xml_factories.crafting_speed_element import CraftingSpeedElement


class CraftingSpeedFrame:
    crafting_speed_scale: Scale
    row = 1
    initial_scale_value = None

    def __init__(self, element: CraftingSpeedElement):
        self.element = element

    def render(self, master: tk):
        label_frame = tk.Frame(master=master, pady=20, padx=20)
        label_frame.grid(row=self.row, column=0)
        label = tk.Label(master=label_frame, text="Crafting Speed")
        label.pack()

        crafting_speed_frame = tk.Frame(master=master, padx=20)
        crafting_speed_frame.grid(row=self.row, column=1)
        crafting_speed_scale = tk.Scale(
            master=crafting_speed_frame, from_=0.1, to_=1.0,
            orient=tk.HORIZONTAL, resolution=0.1
        )
        initial_scale_value = self.element.get_timeout()
        crafting_speed_scale.set(initial_scale_value)
        crafting_speed_scale.pack()
        self.crafting_speed_scale = crafting_speed_scale

        apply_button_frame = tk.Frame(master=master, padx=20)
        apply_button_frame.grid(row=self.row, column=3)
        apply_button = tk.Button(master=apply_button_frame, text="Apply")
        apply_button.bind('<Button-1>', self.handle_apply_event)
        apply_button.pack()

    def handle_apply_event(self, event):
        scale_value = self.crafting_speed_scale.get()
        self.element.set_timeout(scale_value)
