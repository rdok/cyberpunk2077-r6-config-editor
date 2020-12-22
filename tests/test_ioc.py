from argparse import ArgumentParser
from tkinter import Tk

import pytest

# from src.configuration import Configuration
from src.config import Config
from src.ioc import IOC
from src.transformers.key_transformer import KeyTransformer
from src.xml_factories.button_factory import ButtonFactory
from src.xml_factories.crafting_speed_element import CraftingSpeedElement


def expected_dependencies():
    return [Tk, Config, ArgumentParser, KeyTransformer, ButtonFactory,
            CraftingSpeedElement]


ioc = IOC()


class TestIOC:
    @pytest.mark.parametrize("expected_class", expected_dependencies())
    def test_it_loads_dependencies(self, expected_class):
        assert ioc.has(expected_class) is True
        assert isinstance(ioc.get(expected_class), expected_class) is True

    def test_it_manually_sets_a_dependency(self):
        assert ioc.has('ManualClass') is False
        ioc.set('ManualClass', 'ManualClassObject')
        assert ioc.has('ManualClass') is True
