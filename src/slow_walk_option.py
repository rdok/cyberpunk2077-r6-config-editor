import tkinter as tk
from xml.etree import ElementTree

from src.slow_walk_element import SlowWalkElement


class SlowWalkOption():
    def __init__(self, slow_walk_element: SlowWalkElement, filename):
        self.filename = filename
        self.slow_walk_element = slow_walk_element

    def create(self, master: tk.Frame):
        self.mapping_key = None
        self.speed = None

        # slow_walk_option.grid(row=0, column=0)

        frame = tk.Frame(master=master)
        frame.grid(row=0, column=0)
        label = tk.Label(master=frame, text="Slow walk")
        label.pack()

        frame = tk.Frame(master=master, padx=20)
        frame.grid(row=0, column=1)
        self.mapping_entry = tk.Entry(frame, textvariable=self.mapping_key)
        self.mapping_entry.insert(0, 'No mapping key set')
        self.mapping_entry.bind('<KeyRelease>', self.handle_mapping_key_changed)
        self.mapping_entry.bind('<Button-1>', self.handle_mapping_entry_clicked)
        self.mapping_entry.pack()

        frame = tk.Frame(master=master)
        frame.grid(row=0, column=3)
        apply_button = tk.Button(master=frame, text="Apply")
        apply_button.bind('<Button-1>', self.handle_apply_event)
        apply_button.pack()

    def handle_apply_event(self, event):
        mapping_entry = self.mapping_entry.get()

        tree = ElementTree.parse(self.filename)

        y_axis_xpath = './/mapping[@name="LeftY_Axis"][@type="Axis"]'
        self.slow_walk_element.append_to(y_axis_xpath, tree, mapping_entry)

        x_axis_xpath = './/mapping[@name="LeftX_Axis"][@type="Axis"]'
        self.slow_walk_element.append_to(x_axis_xpath, tree, mapping_entry)

        tree.write(self.filename)

    def handle_mapping_entry_clicked(self, event):
        self.mapping_entry.delete(0, tk.END)

    def handle_mapping_key_changed(self, event):
        self.mapping_entry.delete(0, tk.END)
        self.mapping_entry.insert(0, event.keysym)
