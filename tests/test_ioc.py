from argparse import ArgumentParser
from tkinter import Tk

import pytest

# from src.configuration import Configuration
from src.config import Config
from src.ioc import IOC
from src.services.element_appender import ElementAppender


def expected_dependecies():
    return [ElementAppender, ArgumentParser, Tk, Config]


ioc = IOC()


class TestIOC():
    @pytest.mark.parametrize("expected_class", expected_dependecies())
    def test_it_loads_dependencies(self, expected_class):
        assert ioc.has(expected_class) is True
        assert isinstance(ioc.get(expected_class), expected_class) is True

    def test_it_manually_sets_a_dependecy(self):
        assert ioc.has('ManualClass') is False
        ioc.set('ManualClass', 'ManualClassObject')
        assert ioc.has('ManualClass') is True
