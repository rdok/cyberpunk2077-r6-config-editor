import unittest
from unittest.mock import patch, MagicMock

from src.xml_editors.CustomTreeBuilder import CustomTreeBuilder
from src.xml_editors.Editor import Editor

xpath_mock = MagicMock(spec=str)
parser_mock = MagicMock(spec=CustomTreeBuilder)
filename_mock = MagicMock(spec=str)


class AnonymousEditor(Editor):
    def get_xpath(self) -> str:
        return xpath_mock


class TestEditor(unittest.TestCase):
    @patch('src.xml_editors.Editor.ElementTree')
    @patch('src.xml_editors.Editor.XMLParser')
    def test_it_should_find_itself(self, xml_parser, element_tree):
        editor = AnonymousEditor(filename_mock)

        xpath_mock = MagicMock()
        root = element_tree.parse.return_value
        expected_element = root.find.return_value

        actual_element = editor.find(xpath_mock)

        element_tree.parse.assert_called()
        root.find.assert_called_once_with(xpath_mock)
        self.assertEqual(expected_element, actual_element)

    @patch('src.xml_editors.Editor.ElementTree')
    @patch('src.xml_editors.Editor.XMLParser')
    def test_it_should_write_to_file(self, xml_parser, element_tree):
        editor = AnonymousEditor(filename_mock)
        editor.write()
        root = element_tree.parse.return_value
        root.write.assert_called_once_with(
            filename_mock, xml_declaration=True, encoding='utf8')
