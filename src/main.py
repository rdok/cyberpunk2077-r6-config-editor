from argparse import ArgumentParser

from src.config import Config
from src.gui import GUI
from src.ioc import IOC


def main(ioc: IOC):
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
    config: Config = ioc.get(Config)
    config.set_input_user_mappings_path(args.input_user_mappings_path)
    config.set_input_contexts_path(args.input_contexts_path)

    gui: GUI = ioc.get(GUI)
    gui.create_remap_walk_frame()
    gui.create_crafting_speed_frame()
    gui.mainloop()


if __name__ == "__main__":
    main(IOC())
