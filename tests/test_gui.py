import unittest
from types import SimpleNamespace
from unittest.mock import MagicMock

from src.framers.slow_walk_creator import SlowWalkCreator
from src.gui import GUI
from src.ioc import IOC

slow_walk_creator = MagicMock(spec=SlowWalkCreator)

ioc = IOC()
ioc.set(SlowWalkCreator, slow_walk_creator)


class TestGUI(unittest.TestCase):
    def test_it_creates_slow_walk_framer(self):
        args = SimpleNamespace(input_user_mappings_path='mocked_path')
        gui = GUI(ioc, args)
        gui.create_slow_walk_mapper()
        slow_walk_creator.create.assert_called_once()

