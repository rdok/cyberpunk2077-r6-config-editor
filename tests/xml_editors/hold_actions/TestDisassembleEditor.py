import unittest
from unittest.mock import MagicMock, patch

from src.Config import Config
from src.xml_editors.hold_actions.DisassembleEditor import DisassembleEditor
from src.xml_editors.hold_actions.HoldActionEditor import HoldActionEditor


class TestDisassembleEditor(unittest.TestCase):
    @patch('src.xml_editors.Editor.ElementTree')
    def setUp(self, element_tree) -> None:
        config = MagicMock(spec=Config)
        self.editor = DisassembleEditor(config=config)

    def test_it_instantiates_hold_action_editor(self):
        self.assertIsInstance(self.editor, HoldActionEditor)

    def test_it_maintains_xpath_to_element(self):
        xpath = './/hold[@action="disassemble_item"]'
        self.assertEqual(xpath, self.editor.get_xpath())
