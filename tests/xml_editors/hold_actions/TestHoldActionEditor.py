import unittest
from unittest.mock import MagicMock, patch

import src
from src.Config import Config
from src.xml_editors.CustomTreeBuilder import CustomTreeBuilder
from src.xml_editors.hold_actions.HoldActionEditor import HoldActionEditor

xpath_mock = MagicMock(spec=str)


class AnonymousEditor(HoldActionEditor):
    def get_xpath(self) -> str:
        return xpath_mock


class TestHoldActionEditor(unittest.TestCase):
    @patch('src.xml_editors.Editor.ElementTree')
    def setUp(self, element_tree) -> None:
        self.config = MagicMock(spec=Config)
        self.parser = MagicMock(spec=CustomTreeBuilder)
        self.editor = AnonymousEditor(config=self.config)

    @patch.object(src.xml_editors.Editor.Editor, 'get')
    def test_it_should_fetch_the_current_timeout_value(self, get):
        expected_element = get.return_value
        expected_timeout = expected_element.get.return_value

        actual_timeout = self.editor.get_timeout()

        self.assertEqual(expected_timeout, actual_timeout)

    @patch.object(src.xml_editors.Editor.Editor, 'write')
    @patch('src.xml_editors.Editor.ElementTree')
    def test_it_should_save_the_new_timeout_value(self, element_tree, write):
        self.editor.get = MagicMock()
        element = self.editor.get.return_value
        new_timeout = MagicMock()

        self.editor.set_timeout(new_timeout)

        self.editor.get.assert_called_once()
        element.set.assert_called_once_with('timeout', str(new_timeout))
        write.assert_called_once()
