import unittest
from unittest.mock import MagicMock, patch

import pytest

from src.config import Config
from src.xml_factories.crafting_speed_element import CraftingSpeedElement


class TestCraftingSpeedElement(unittest.TestCase):
    config = MagicMock(spec=Config)
    crafting_speed_element = CraftingSpeedElement(config=config)

    @patch('src.xml_factories.crafting_speed_element.ElementTree')
    def test_it_should_fetch_the_current_speed_value(self, element_tree):
        filename = self.config.get_input_contexts_path.return_value
        root = element_tree.parse.return_value
        expected_crafting_speed_element = root.find.return_value
        expected_crafting_speed_timeout = \
            expected_crafting_speed_element.get.return_value

        actual_timeout = self.crafting_speed_element.get_timeout()

        element_tree.parse.assert_called_once_with(filename)
        root.find.assert_called_once_with('.//hold[@action="craft_item"]')
        expected_crafting_speed_element.get.assert_called_once_with('timeout')
        self.assertEqual(expected_crafting_speed_timeout, actual_timeout)

    @pytest.mark.skip()
    def test_it_should_save_the_new_speed_value(self):
        pass
