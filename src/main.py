import os
import tkinter as tk
from argparse import ArgumentParser

# from src.slow_walk_element import SlowWalkElement
from src.gui import GUI
from src.slow_walk_element import SlowWalkElement

DIR_NAME = os.path.dirname(__file__)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-i",
        "--input_user_mappings_path",
        dest="input_user_mappings_path",
        default='r6/config/inputUserMappings.xml'
    )
    args = parser.parse_args()

    dependencies = {SlowWalkElement.__name__: SlowWalkElement()}

    root = tk.Tk()
    gui = GUI(root, args, dependencies)
    gui.mainloop()
