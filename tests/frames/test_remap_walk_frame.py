import unittest
from unittest.mock import MagicMock

from src.frames.remap_walk_frame import RemapWalkFrame
from src.xml_editors.walk_key_editor import WalkKeyEditor


class TestRemapWalkFrame(unittest.TestCase):
    walk_element: MagicMock
    mapping_entry: MagicMock
    remap_walk_frame: RemapWalkFrame

    def setUp(self) -> None:
        self.walk_element = MagicMock(WalkKeyEditor)
        self.mapping_entry = MagicMock()
        self.remap_walk_frame = RemapWalkFrame(
            walk_element=self.walk_element,
            walk_key=MagicMock()
        )
        self.remap_walk_frame.mapping_entry = self.mapping_entry

    def test_it_handles_apply_event(self):
        self.remap_walk_frame.handle_apply_event(None)

        self.walk_element.write \
            .assert_called_once_with(self.mapping_entry.get.return_value)

    def test_it_handles_entry_clicked_event(self):
        self.remap_walk_frame.handle_entry_clicked(None)
        self.mapping_entry.delete.assert_called_once_with(0, 'end')

    def test_it_handles_entry_changed_event(self):
        event = MagicMock()
        self.remap_walk_frame.handle_entry_changed(event)
        self.mapping_entry.delete.assert_called_once_with(0, 'end')
        self.mapping_entry.insert.assert_called_once_with(0, event.keysym)
