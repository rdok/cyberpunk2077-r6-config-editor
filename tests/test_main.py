from argparse import ArgumentParser
from unittest.mock import MagicMock

from src import main
from src.config import Config
from src.gui import GUI
from src.ioc import IOC

ioc = IOC()

argument_parser = MagicMock(spec=ArgumentParser)
ioc.set(ArgumentParser, argument_parser)

gui = MagicMock(spec=GUI)
ioc.set(GUI, gui)

config = MagicMock(spec=Config)
ioc.set(Config, config)


def test_it_creates_the_gui():
    main.main(ioc)

    argument_parser.add_argument.assert_called_once_with(
        "-i",
        "--input_user_mappings_path",
        dest="input_user_mappings_path",
        default='r6/config/inputUserMappings.xml'
    )

    config.set_input_user_mappings_path.assert_called_with(
        argument_parser.parse_args.return_value.input_user_mappings_path)
    gui.mainloop.assert_called_once()


def test_it_creates_remap_walk_frame():
    gui.create_remap_walk_frame.assert_called_once()


def test_it_creates_crafting_speed_frame():
    gui.create_crafting_speed_frame.assert_called_once()
