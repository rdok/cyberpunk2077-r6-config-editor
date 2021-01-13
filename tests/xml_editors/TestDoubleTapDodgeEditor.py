import unittest
from unittest.mock import MagicMock, patch

import src
from src.Config import Config
from src.xml_editors.CustomTreeBuilder import CustomTreeBuilder
from src.xml_editors.DoubleTapDodgeEditor import DoubleTapDodgeEditor
from src.xml_editors.Editor import Editor


class TestCraftingEditor(unittest.TestCase):
    def setUp(self) -> None:
        config = MagicMock(spec=Config)
        builder = MagicMock(spec=CustomTreeBuilder)
        self.editor = DoubleTapDodgeEditor(config=config, parser=builder)

    def test_it_is_instantiated_as_an_editor(self):
        self.assertIsInstance(self.editor, Editor)

    def test_it_maintains_xpath_to_elements(self):
        xpaths = {
            'forward': './/multitap[@action="DodgeForward"]',
            'right': './/multitap[@action="DodgeRight"]',
            'back': './/multitap[@action="DodgeBack"]',
            'left': './/multitap[@action="DodgeLeft"]',
        }

        self.assertEqual(xpaths, self.editor.get_xpath())

    @patch.object(src.xml_editors.Editor.Editor, 'find')
    @patch.object(
        src.xml_editors.DoubleTapDodgeEditor.DoubleTapDodgeEditor, 'get_xpath')
    def test_it_finds_out_if_double_tap_dodge_is_enabled(self, get_xpath, find):
        find.return_value.get.return_value = 2
        self.assertEqual(True, self.editor.is_enabled())

        get_xpath.return_value.get.assert_called_once_with('forward')
        find.assert_called_once_with(get_xpath.return_value.get.return_value)
        find.return_value.get.assert_called_once_with('count')

    @patch.object(src.xml_editors.Editor.Editor, 'find')
    @patch.object(
        src.xml_editors.DoubleTapDodgeEditor.DoubleTapDodgeEditor, 'get_xpath')
    def test_it_finds_out_if_double_tap_dodge_is_disabled(self, get_xpath, find):
        find.return_value.get.return_value = 55
        self.assertEqual(False, self.editor.is_enabled())
