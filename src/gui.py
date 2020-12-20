import os
import tkinter as tk

from src.slow_walk_element import SlowWalkElement
from src.slow_walk_option import SlowWalkOption


class GUI(tk.Frame):
    def __init__(self, window, args, ioc):
        super().__init__(window)

        master = tk.Frame(master=window)
        master.grid(row=0, column=0, padx=20, pady=20)

        dir_name = os.path.dirname(__file__)
        input_user_mappings_path = os.path \
            .join(dir_name, args.input_user_mappings_path)

        slow_walk_option = SlowWalkOption(
            slow_walk_element=ioc.get(SlowWalkElement.__name__),
            filename=input_user_mappings_path
        )

        slow_walk_option.create(master=master)
        # filename, ioc, master = master, padx = 20, pady = 20,

# def create_apply_action(self, actions_frame):
#     frame = tk.Frame(master=actions_frame)
#     frame.grid(row=0, column=0)
#     apply_walk_button = tk.Button(master=frame, text="Apply")
#     apply_walk_button.pack()
