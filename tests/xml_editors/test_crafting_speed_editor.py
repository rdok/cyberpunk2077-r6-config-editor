import unittest
from unittest.mock import MagicMock, patch

from src.config import Config
from src.xml_editors.CustomParser import CustomParser
from src.xml_editors.crafting_speed_element import CraftingSpeedEditor


class TestCraftingSpeedElement(unittest.TestCase):
    def setUp(self) -> None:
        self.config = MagicMock(spec=Config)
        self.custom_parser = MagicMock(spec=CustomParser)
        self.crafting_speed_editor = CraftingSpeedEditor(
            config=self.config,
            parser=self.custom_parser
        )

    @patch('src.xml_editors.crafting_speed_element.ElementTree')
    def test_it_should_fetch_the_current_speed_value(self, element_tree):
        self.crafting_speed_editor.get = MagicMock()
        expected_element = self.crafting_speed_editor.get.return_value
        expected_timeout = expected_element.get.return_value

        actual_timeout = self.crafting_speed_editor.get_timeout()

        self.assertEqual(expected_timeout, actual_timeout)

    @patch('src.xml_editors.crafting_speed_element.ElementTree')
    @patch('src.xml_editors.crafting_speed_element.XMLParser')
    def test_it_should_locate_itself(self, xml_parser, element_tree):
        filename = self.config.get_input_contexts_path.return_value
        root = element_tree.parse.return_value
        expected_element = root.find.return_value

        actual_element = self.crafting_speed_editor.get()

        parser = xml_parser.return_value
        element_tree.parse.assert_called_once_with(filename, parser=parser)
        root.find.assert_called_once_with('.//hold[@action="craft_item"]')
        self.assertEqual(expected_element, actual_element)

    @patch('src.xml_editors.crafting_speed_element.ElementTree')
    def test_it_should_save_the_new_speed_value(self, element_tree):
        self.crafting_speed_editor.get = MagicMock()
        root = element_tree.parse.return_value
        self.crafting_speed_editor.root = root
        element = self.crafting_speed_editor.get.return_value
        new_timeout = MagicMock()

        self.crafting_speed_editor.set_timeout(new_timeout)

        self.crafting_speed_editor.get.assert_called_once()
        element.set.assert_called_once_with('timeout', str(new_timeout))
        root.write.assert_called_once()
