import unittest
from tkinter import Scale, Tk
from unittest.mock import MagicMock, patch

from src.frames.hold_actions.HoldActionFrame import HoldActionFrame
from src.xml_editors.hold_actions.HoldActionEditor import HoldActionEditor


class AnonymousHoldActionEditor(HoldActionEditor):
    def __init__(self):
        super().__init__(MagicMock(), MagicMock())


class AnonymousHoldActionFrame(HoldActionFrame):
    def __init__(self, editor: HoldActionEditor):
        super().__init__(editor)

    def label_text(self) -> str:
        pass

    def from_(self) -> float:
        pass

    def to_(self) -> float:
        pass

    def resolution(self) -> float:
        pass

    def frame_row(self) -> int:
        pass


class TestHoldActionFrame(unittest.TestCase):
    master = MagicMock(spec=Tk)
    editor = MagicMock(spec=AnonymousHoldActionEditor)
    frame = AnonymousHoldActionFrame(editor=editor)
    scale = MagicMock(spec=Scale)
    frame.scale = scale

    def test_it_handles_apply_event(self):
        self.frame.handle_apply_event(None)
        timeout = self.scale.get.return_value
        self.editor.set_timeout.assert_called_once_with(timeout)

    @patch('src.frames.hold_actions.HoldActionFrame.ButtonFrame')
    @patch('src.frames.hold_actions.HoldActionFrame.Scale')
    @patch('src.frames.hold_actions.HoldActionFrame.Frame')
    def test_it_sets_initial_timeout(self, frame, scale, btn):
        master = MagicMock(spec=Tk)
        initial_scale_value = self.editor.get_timeout.return_value
        self.frame.render(master=master)
        scale.return_value.set.assert_called_once_with(initial_scale_value)
