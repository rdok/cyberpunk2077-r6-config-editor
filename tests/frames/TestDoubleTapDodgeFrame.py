import unittest
from unittest.mock import MagicMock

from src.frames.DoubleTapDodgeFrame import DoubleTapDodgeFrame
from src.xml_editors.DoubleTapDodgeEditor import DoubleTapDodgeEditor


class TestDoubleTapDodgeFrame(unittest.TestCase):
    editor: DoubleTapDodgeEditor
    frame: DoubleTapDodgeFrame

    def setUp(self) -> None:
        self.editor = MagicMock(DoubleTapDodgeEditor)
        self.frame = DoubleTapDodgeFrame(toggle_editor=self.editor)

    def test_it_maintains_the_label_text(self):
        self.assertEqual("DOUBLE TAP DODGE", self.frame.label_text())

    def test_it_maintains_the_frame_position(self):
        self.assertEqual(4, self.frame.frame_row())

    def test_it_dispatches_disable_to_editor(self):
        self.frame.dispatch_disable_event()
        self.editor.disable.assert_called_once()

    def test_it_dispatches_enable_to_editor(self):
        self.frame.dispatch_enable_event()
        self.editor.enable.assert_called_once()
