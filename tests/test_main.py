from argparse import ArgumentParser
from tkinter import Tk
from unittest.mock import MagicMock, patch

from src import main
from src.services.slow_walk_element import SlowWalkElement

argument_parser = MagicMock(spec=ArgumentParser)
tkinter = MagicMock(spec=Tk)

ioc = {
    SlowWalkElement.__name__: MagicMock(spec=SlowWalkElement),
    ArgumentParser.__name__: argument_parser,
    Tk.__name__: tkinter,
}


@patch('src.main.GUI')
def test_it_creates_the_gui(gui):
    main.main(ioc)

    argument_parser.add_argument.assert_called_once_with(
        "-i",
        "--input_user_mappings_path",
        dest="input_user_mappings_path",
        default='r6/config/inputUserMappings.xml'
    )

    gui.assert_called_once_with(
        tkinter, argument_parser.parse_args.return_value, ioc
    )
    gui.return_value.mainloop.assert_called_once()