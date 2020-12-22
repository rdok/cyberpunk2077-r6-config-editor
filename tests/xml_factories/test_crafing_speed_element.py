import unittest
from unittest.mock import MagicMock, patch

import pytest

from src.config import Config
from src.xml_factories.crafting_speed_element import CraftingSpeedElement


class TestCraftingSpeedElement(unittest.TestCase):
    config = MagicMock(spec=Config)
    crafting_speed_element = CraftingSpeedElement(config=config)

    @pytest.mark.skip()
    @patch('src.xml_factories.crafting_speed_element.ElementTree')
    def test_it_should_fetch_the_current_speed_value(self, element_tree):
        # get the path of the xml from the config
        filename = self.config.get_input_contexts_path.return_value

        element_tree.parse.assert_called_once_with(filename)
        root = element_tree.parse.return_value

        root.find.assert_called_once_with(
            './/mapping[@name="LeftY_Axis"][@type="Axis"]')

        # locate the element using xpath

        # get the value
        # return the value

    @pytest.mark.skip()
    def test_it_should_save_the_new_speed_value(self):
        pass
