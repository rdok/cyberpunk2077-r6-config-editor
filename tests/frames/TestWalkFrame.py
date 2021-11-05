import unittest
from unittest.mock import MagicMock

from src.frames.WalkFrame import WalkFrame
from src.xml_editors.walk_key_editor import WalkEditor


class TestWalkFrame(unittest.TestCase):
    element: MagicMock
    mapping_entry: MagicMock
    walk_frame: WalkFrame

    def setUp(self) -> None:
        self.element = MagicMock(WalkEditor)
        self.mapping_entry = MagicMock()
        self.walk_frame = WalkFrame(walk_editor=self.element, walk_key=MagicMock())
        self.walk_frame.mapping_entry = self.mapping_entry
        self.walk_frame.tk = MagicMock()
        self.walk_frame.apply_button = MagicMock()

    def test_it_handles_apply_event(self):
        self.walk_frame.handle_apply_event(None)

        self.element.write.assert_called_once_with(self.mapping_entry.get.return_value)
        self.walk_frame.apply_button.config.assert_called_once_with(text="Done")
        self.walk_frame.apply_button.pack.assert_called_once()

    def test_it_handles_entry_clicked_event(self):
        self.walk_frame.handle_entry_clicked(None)
        self.mapping_entry.delete.assert_called_once_with(0, "end")

    def test_it_handles_entry_changed_event(self):
        event = MagicMock()
        self.walk_frame.handle_entry_changed(event)
        self.mapping_entry.delete.assert_called_once_with(0, "end")
        self.mapping_entry.insert.assert_called_once_with(0, event.keysym)
