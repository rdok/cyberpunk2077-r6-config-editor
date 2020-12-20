import tkinter as tk


class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.slow_walk_btn_value = None

        self.master = master

        options_frame = tk.Frame(master=self.master, padx=20, pady=20)
        options_frame.grid(row=0, column=0)
        self.create_slow_walk_option(options_frame)

        actions_frame = tk.Frame(master=self.master, padx=20, pady=20)
        actions_frame.grid(row=1, column=0)
        self.create_apply_action(actions_frame)

    def create_slow_walk_option(self, options_frame):
        frame = tk.Frame(master=options_frame)
        frame.grid(row=0, column=0)
        slow_walk_label = tk.Label(master=frame, text="Slow walk")
        slow_walk_label.pack()

        frame = tk.Frame(master=options_frame)
        frame.grid(row=0, column=1)
        slow_walk_entry = tk.Entry(master=frame,
                                   textvariable=self.slow_walk_btn_value)
        slow_walk_entry.insert(0, 'Find shortcut')
        slow_walk_entry.pack()

    def create_apply_action(self, actions_frame):
        frame = tk.Frame(master=actions_frame)
        frame.grid(row=0, column=0)
        apply_walk_button = tk.Button(master=frame, text="Apply")
        apply_walk_button.pack()
