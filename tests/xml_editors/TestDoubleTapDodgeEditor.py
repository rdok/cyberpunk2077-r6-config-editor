import unittest
from unittest.mock import MagicMock, patch, call

import src
from src.Config import Config
from src.xml_editors.ContextsEditor import ContextsEditor
from src.xml_editors.CustomTreeBuilder import CustomTreeBuilder
from src.xml_editors.DoubleTapDodgeEditor import DoubleTapDodgeEditor


class TestDoubleTapDodgeEditor(unittest.TestCase):
    editor: DoubleTapDodgeEditor
    xpaths = {
        'forward': './/multitap[@action="DodgeForward"]',
        'right': './/multitap[@action="DodgeRight"]',
        'back': './/multitap[@action="DodgeBack"]',
        'left': './/multitap[@action="DodgeLeft"]',
    }

    @patch('src.xml_editors.Editor.ElementTree')
    def setUp(self, element_tree) -> None:
        self.config = MagicMock(spec=Config)
        self.builder = MagicMock(spec=CustomTreeBuilder)
        self.editor = DoubleTapDodgeEditor(
            config=self.config, parser=self.builder
        )

    def test_it_is_instantiated_as_an_editor(self):
        self.assertIsInstance(self.editor, ContextsEditor)

    def test_it_maintains_xpath_to_elements(self):
        self.assertEqual(self.xpaths, self.editor.get_xpath())

    @patch.object(src.xml_editors.Editor.Editor, 'find')
    @patch.object(
        src.xml_editors.DoubleTapDodgeEditor.DoubleTapDodgeEditor, 'get_xpath')
    def test_it_finds_out_if_double_tap_dodge_is_enabled(self, get_xpath, find):
        find.return_value.get.return_value = '2'
        self.assertEqual(True, self.editor.is_enabled())

        get_xpath.return_value.get.assert_called_once_with('forward')
        find.assert_called_once_with(get_xpath.return_value.get.return_value)
        find.return_value.get.assert_called_once_with('count')

    @patch.object(src.xml_editors.Editor.Editor, 'find')
    @patch.object(
        src.xml_editors.DoubleTapDodgeEditor.DoubleTapDodgeEditor, 'get_xpath')
    def test_it_finds_out_if_double_tap_dodge_is_disabled(self,
        get_xpath, find):
        find.return_value.get.return_value = '55'
        self.assertEqual(False, self.editor.is_enabled())

    @patch.object(src.xml_editors.DoubleTapDodgeEditor.DoubleTapDodgeEditor,
        'disable_dodge')
    @patch('src.xml_editors.Editor.ElementTree')
    @patch.object(src.xml_editors.Editor.Editor, 'write')
    def test_it_may_disable_double_tap_doge(self,
        write, element_tree, disable_dodge):
        editor = DoubleTapDodgeEditor(config=self.config, parser=self.builder)
        editor.xpaths = {'alpha': 'alpha-path', 'beta': 'beta-path'}

        editor.disable()

        calls = [call('alpha-path'), call('beta-path')]
        disable_dodge.assert_has_calls(calls)
        write.assert_called_once()

    @patch.object(src.xml_editors.DoubleTapDodgeEditor.DoubleTapDodgeEditor,
        'enable_dodge')
    @patch('src.xml_editors.Editor.ElementTree')
    @patch.object(src.xml_editors.Editor.Editor, 'write')
    def test_it_may_enable_double_tap_doge(self,
        write, element_tree, enable_dodge):
        editor = DoubleTapDodgeEditor(config=self.config, parser=self.builder)
        editor.xpaths = {'alpha': 'alpha-path', 'beta': 'beta-path'}
        editor.enable()
        calls = [call('alpha-path'), call('beta-path')]
        enable_dodge.assert_has_calls(calls)
        write.assert_called_once()
