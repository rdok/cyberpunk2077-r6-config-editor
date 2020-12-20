from argparse import ArgumentParser
from unittest.mock import MagicMock, patch

from src import main
from src.ioc import IOC

ioc = IOC()
argument_parser = MagicMock(spec=ArgumentParser)
ioc.set(ArgumentParser, argument_parser)


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
        ioc=ioc, args=argument_parser.parse_args.return_value
    )

    gui.return_value.create_slow_walk_mapper.assert_called_once()
    gui.return_value.mainloop.assert_called_once()
