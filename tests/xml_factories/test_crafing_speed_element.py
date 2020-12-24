import unittest
from unittest.mock import MagicMock, patch

from src.config import Config
from src.xml_factories.crafting_speed_element import CraftingSpeedElement


class TestCraftingSpeedElement(unittest.TestCase):
    def setUp(self) -> None:
        self.config = MagicMock(spec=Config)
        self.element_modifier = CraftingSpeedElement(config=self.config)

    @patch('src.xml_factories.crafting_speed_element.ElementTree')
    def test_it_should_fetch_the_current_speed_value(self, element_tree):
        self.element_modifier.get = MagicMock()
        expected_element = self.element_modifier.get.return_value
        expected_timeout = expected_element.get.return_value

        actual_timeout = self.element_modifier.get_timeout()

        self.assertEqual(expected_timeout, actual_timeout)

    @patch('src.xml_factories.crafting_speed_element.ElementTree')
    def test_it_should_locate_itself(self, element_tree):
        filename = self.config.get_input_contexts_path.return_value
        root = element_tree.parse.return_value
        expected_element = root.find.return_value

        actual_element = self.element_modifier.get()

        element_tree.parse.assert_called_once_with(filename)
        root.find.assert_called_once_with('.//hold[@action="craft_item"]')
        self.assertEqual(expected_element, actual_element)

    @patch('src.xml_factories.crafting_speed_element.ElementTree')
    def test_it_should_save_the_new_speed_value(self, element_tree):
        self.element_modifier.get = MagicMock()
        root = element_tree.parse.return_value
        self.element_modifier.root = root
        element = self.element_modifier.get.return_value
        new_timeout = MagicMock()

        self.element_modifier.set_timeout(new_timeout)

        self.element_modifier.get.assert_called_once()
        element.set.assert_called_once_with('timeout', str(new_timeout))
        root.write.assert_called_once()
