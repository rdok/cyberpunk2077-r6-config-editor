import tkinter
from argparse import ArgumentParser
from tkinter import messagebox

from src.config import Config
from src.gui import GUI
from src.ioc import IOC


def main(ioc: IOC):
    gui: GUI = ioc.get(GUI)
    gui.create_remap_walk_frame()
    gui.create_crafting_speed_frame()
    gui.mainloop()


def configure_app(ioc: IOC):
    argument_parser = ioc.get(ArgumentParser)
    argument_parser.add_argument(
        "-i",
        "--input_user_mappings_path",
        dest="input_user_mappings_path",
        default='r6/config/inputUserMappings.xml'
    )
    argument_parser.add_argument(
        "-ic",
        "--input_contexts_path",
        dest="input_contexts_path",
        default='r6/config/inputContexts.xml'
    )
    args = argument_parser.parse_args()
    config = ioc.get(Config)
    config.set_input_user_mappings_path(args.input_user_mappings_path)
    config.set_input_contexts_path(args.input_contexts_path)
    ioc.set(Config, config)
    ioc.instantiate_dependencies()

    return ioc


if __name__ == "__main__":
    ioc = IOC()
    ioc = configure_app(ioc=ioc)
    try:
        main(ioc)
    except FileNotFoundError as err:
        root = tkinter.Tk()
        root.withdraw()
        config: Config = ioc.get(Config)
        message = '\n\nApp should be run from the installation directory.'
        error = '{0} {1}'.format(err, message)
        messagebox.showerror(config.app_name(), error)
    except Exception as err:
        root = tkinter.Tk()
        root.withdraw()
        config: Config = ioc.get(Config)
        messagebox.showerror(config.app_name(), err)
