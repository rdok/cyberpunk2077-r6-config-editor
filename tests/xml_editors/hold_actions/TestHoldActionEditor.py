import unittest
from unittest.mock import MagicMock, patch

from src.Config import Config
from src.xml_editors.CustomTreeBuilder import CustomTreeBuilder
from src.xml_editors.hold_actions.HoldActionEditor import HoldActionEditor

xpath_mock = MagicMock(spec=str)


class AnonymousEditor(HoldActionEditor):
    def get_xpath(self) -> str:
        return xpath_mock


class TestHoldActionEditor(unittest.TestCase):
    def setUp(self) -> None:
        self.config = MagicMock(spec=Config)
        self.parser = MagicMock(spec=CustomTreeBuilder)
        self.editor = AnonymousEditor(config=self.config, parser=self.parser)

    @patch('src.xml_editors.hold_actions.HoldActionEditor.ElementTree')
    def test_it_should_fetch_the_current_timeout_value(self, element_tree):
        self.editor.get = MagicMock()
        expected_element = self.editor.get.return_value
        expected_timeout = expected_element.get.return_value

        actual_timeout = self.editor.get_timeout()

        self.assertEqual(expected_timeout, actual_timeout)

    @patch('src.xml_editors.hold_actions.HoldActionEditor.ElementTree')
    @patch('src.xml_editors.hold_actions.HoldActionEditor.XMLParser')
    def test_it_should_locate_itself(self, xml_parser, element_tree):
        filename = self.config.get_input_contexts_path.return_value
        root = element_tree.parse.return_value
        expected_element = root.find.return_value

        actual_element = self.editor.get()

        parser = xml_parser.return_value
        element_tree.parse.assert_called_once_with(filename, parser=parser)
        root.find.assert_called_once_with(xpath_mock)
        self.assertEqual(expected_element, actual_element)

    @patch('src.xml_editors.hold_actions.HoldActionEditor.ElementTree')
    def test_it_should_save_the_new_timeout_value(self, element_tree):
        self.editor.get = MagicMock()
        root = element_tree.parse.return_value
        self.editor.root = root
        element = self.editor.get.return_value
        new_timeout = MagicMock()

        self.editor.set_timeout(new_timeout)

        self.editor.get.assert_called_once()
        element.set.assert_called_once_with('timeout', str(new_timeout))
        root.write.assert_called_once()
