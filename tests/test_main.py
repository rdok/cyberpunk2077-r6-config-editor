from argparse import ArgumentParser
from unittest.mock import MagicMock

from src import main
from src.gui import GUI
from src.ioc import IOC

ioc = IOC()
argument_parser = MagicMock(spec=ArgumentParser)
ioc.set(ArgumentParser, argument_parser)
gui = MagicMock(spec=GUI)
ioc.set(GUI, gui)


def test_it_creates_the_gui():
    main.main(ioc)

    argument_parser.add_argument.assert_called_once_with(
        "-i",
        "--input_user_mappings_path",
        dest="input_user_mappings_path",
        default='r6/config/inputUserMappings.xml'
    )

    gui.create_remap_walk_frame.assert_called_once()
    gui.mainloop.assert_called_once()
