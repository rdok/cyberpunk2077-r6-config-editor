import tkinter as tk
from tkinter import Entry

from src.xml_factories.button_factory import ButtonFactory


class RemapWalkFrame:
    row = 0
    mapping_entry: Entry
    button_factory: ButtonFactory

    def __init__(self, button_factory: ButtonFactory):
        self.button_factory = button_factory

    def render(self, master: tk):
        label_frame = tk.Frame(master=master, pady=20, padx=20)
        label_frame.grid(row=self.row, column=0)
        label = tk.Label(master=label_frame, text="Walk")
        label.pack()

        mapping_entry_frame = tk.Frame(master=master, padx=20)
        mapping_entry_frame.grid(row=self.row, column=1)
        mapping_entry = tk.Entry(mapping_entry_frame)
        mapping_entry.insert(0, 'No mapping key set')
        mapping_entry.bind('<KeyRelease>', self.handle_entry_changed)
        mapping_entry.bind('<Button-1>', self.handle_entry_clicked)
        mapping_entry.pack()
        self.mapping_entry = mapping_entry

        apply_button_frame = tk.Frame(master=master, padx=20)
        apply_button_frame.grid(row=self.row, column=3)
        apply_button = tk.Button(master=apply_button_frame, text="Apply")
        apply_button.bind('<Button-1>', self.handle_apply_event)
        apply_button.pack()

    def handle_apply_event(self, event):
        y_axis_xpath = './/mapping[@name="LeftY_Axis"][@type="Axis"]'
        self.button_factory.add(y_axis_xpath, self.mapping_entry.get())

        x_axis_xpath = './/mapping[@name="LeftX_Axis"][@type="Axis"]'
        self.button_factory.add(x_axis_xpath, self.mapping_entry.get())

    def handle_entry_clicked(self, event):
        self.mapping_entry.delete(0, tk.END)

    def handle_entry_changed(self, event):
        self.mapping_entry.delete(0, tk.END)
        self.mapping_entry.insert(0, event.keysym)
