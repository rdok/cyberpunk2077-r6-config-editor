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
    args = argument_parser.parse_args()
    config = ioc.get(Config)
    config.set_input_user_mappings_path(args.input_user_mappings_path)

    gui = ioc.get(GUI)
    gui.create_remap_walk_frame()
    gui.mainloop()


if __name__ == "__main__":
    main(IOC())
