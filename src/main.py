from argparse import ArgumentParser
from tkinter import Tk

from src.gui import GUI
from src.services.slow_walk_element import SlowWalkElement


def main(ioc: dict):
    argument_parser = ioc.get(ArgumentParser.__name__)
    tk = ioc.get(Tk.__name__)

    argument_parser.add_argument(
        "-i",
        "--input_user_mappings_path",
        dest="input_user_mappings_path",
        default='r6/config/inputUserMappings.xml'
    )
    args = argument_parser.parse_args()

    gui = GUI(tk, args, ioc)
    gui.mainloop()


if __name__ == "__main__":
    dependencies = {
        SlowWalkElement.__name__: SlowWalkElement(),
        ArgumentParser.__name__: ArgumentParser(),
        Tk.__name__: Tk(),
    }

    main(dependencies)
