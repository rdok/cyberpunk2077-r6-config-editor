import tkinter
import tkinter as tk

from src.widgets.Button import Button
from src.widgets.ButtonFrame import ButtonFrame
from src.widgets.Entry import Entry
from src.widgets.Frame import Frame
from src.widgets.Label import Label
from src.xml_editors.walk_key_editor import WalkEditor, WalkKey


class WalkFrame:
    walk_key: WalkKey
    row = 0
    mapping_entry: Entry
    walk_editor: WalkEditor
    tk: tk

    def __init__(self, walk_editor: WalkEditor, walk_key: WalkKey):
        self.walk_key = walk_key
        self.walk_editor = walk_editor

    def render(self, master: tk):
        self.tk = tk
        label_frame = Frame(master=master)
        label_frame.grid(row=self.row, column=0)
        label = Label(master=label_frame, text="WALK (HOLD)")
        label.pack()

        entry_frame = Frame(master=master)
        entry_frame.grid(row=self.row, column=1)
        mapping_entry = Entry(master=entry_frame)
        current_key = self.walk_key.find()
        if current_key is None:
            mapping_entry.insert(0, 'CLICK TO SET KEY')
        else:
            key = current_key.get('id').replace('IK_', '')
            mapping_entry.insert(0, key)

        mapping_entry.bind('<KeyRelease>', self.handle_entry_changed)
        mapping_entry.bind('<Button-1>', self.handle_entry_clicked)
        mapping_entry.pack()
        self.mapping_entry = mapping_entry

        frame = Frame(master=master)
        frame.grid(row=self.row, column=2)
        apply_button_frame = ButtonFrame(master=frame)
        apply_button_frame.grid()
        apply_button = Button(master=apply_button_frame, text="APPLY")
        apply_button.bind('<Button-1>', self.handle_apply_event)
        apply_button.pack()

    def handle_apply_event(self, event):
        self.walk_editor.write(self.mapping_entry.get())
        self.tk.messagebox.showinfo(message="Done")

    def handle_entry_clicked(self, event):
        self.mapping_entry.delete(0, tk.END)

    def handle_entry_changed(self, event):
        self.mapping_entry.delete(0, tk.END)
        self.mapping_entry.insert(0, event.keysym)
