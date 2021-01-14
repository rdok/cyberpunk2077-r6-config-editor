import unittest
from unittest.mock import MagicMock

from src.frames.DoubleTapDodgeFrame import DoubleTapDodgeFrame
from src.xml_editors.DoubleTapDodgeEditor import DoubleTapDodgeEditor


class TestDoubleTapDodgeFrame(unittest.TestCase):
    frame: DoubleTapDodgeFrame

    def setUp(self) -> None:
        editor = MagicMock(DoubleTapDodgeEditor)
        self.frame = DoubleTapDodgeFrame(toggle_editor=editor)

    def test_it_maintains_the_label_text(self):
        self.assertEqual('DOUBLE TAP DODGE', self.frame.label_text())

    # todo: move this to double tap dodge
    # def test_it_maintains_the_default_count_value(self):
    #     self.assertEqual(2, self.frame.default_count())

    # def test_it_maintains_the_frame_position(self):
    #     self.assertEqual(4, self.frame.frame_row())



# import unittest
# from tkinter import Scale, Tk
# from unittest.mock import MagicMock, patch
#
# from src.frames.DoubleTapDodgeFrame import MultitapActionFrame
# from src.xml_editors.hold_actions.HoldActionEditor import HoldActionEditor
#
#
# class AnonymousHoldActionEditor(MultitapActionFrame):
#     def __init__(self):
#         super().__init__(MagicMock(), MagicMock())
#
#
# class AnonymousHoldActionFrame(MultitapActionFrame):
#     def __init__(self, editor: HoldActionEditor):
#         super().__init__(editor)
#
#     def label_text(self) -> str:
#         pass
#
#     def from_(self) -> float:
#         pass
#
#     def to_(self) -> float:
#         pass
#
#     def resolution(self) -> float:
#         pass
#
#     def frame_row(self) -> int:
#         pass
#
#
# class TestHoldActionFrame(unittest.TestCase):
#     master = MagicMock(spec=Tk)
#     editor = MagicMock(spec=AnonymousHoldActionEditor)
#     frame = AnonymousHoldActionFrame(editor=editor)
#     scale = MagicMock(spec=Scale)
#     frame.scale = scale
#     frame.tk = MagicMock()
#
#     def test_it_handles_apply_event(self):
#         self.frame.handle_apply_event(None)
#         timeout = self.scale.get.return_value
#         self.editor.set_timeout.assert_called_once_with(timeout)
#         self.frame.tk.messagebox.showinfo \
#             .assert_called_once_with(message="Done")
#
#         # assert count was set to 99
#         # assert count was set to default to 2
#
#         # should have label text 'Disable' if count is not to 2
#         # should have label text 'Enable' if count is not to 99
#
#     @patch('src.frames.hold_actions.HoldActionFrame.ButtonFrame')
#     @patch('src.frames.hold_actions.HoldActionFrame.Scale')
#     @patch('src.frames.hold_actions.HoldActionFrame.Frame')
#     def test_it_sets_initial_timeout(self, frame, scale, btn):
#         master = MagicMock(spec=Tk)
#         initial_scale_value = self.editor.get_timeout.return_value
#         self.frame.render(master=master)
#         scale.return_value.set.assert_called_once_with(initial_scale_value)
