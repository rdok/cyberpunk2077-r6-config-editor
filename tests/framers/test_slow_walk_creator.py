import unittest

from src.config import Config
from src.framers.slow_walk_creator import SlowWalkCreator
from src.ioc import IOC


class TestSlowWalkCreator(unittest.TestCase):
    def test_it_creates_slow_walk_framer(self):
        slow_walk_creator = SlowWalkCreator(config=IOC().get(Config))
        slow_walk_creator.create()
        self.assertTrue(True)
