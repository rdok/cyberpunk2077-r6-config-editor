import unittest
from unittest.mock import MagicMock, call

from src.config import Config
from src.frames.remap_walk_frame import RemapWalkFrame
from src.xml_factories.button_factory import ButtonFactory


class TestRemapWalkFrame(unittest.TestCase):
    button_factory: MagicMock
    mapping_entry: MagicMock
    remap_walk_frame: RemapWalkFrame

    def setUp(self) -> None:
        self.button_factory = MagicMock(ButtonFactory)
        self.mapping_entry = MagicMock()
        self.remap_walk_frame = RemapWalkFrame(
            button_factory=self.button_factory, config=MagicMock(Config))
        self.remap_walk_frame.mapping_entry = self.mapping_entry

    def test_it_handles_apply_event(self):
        self.remap_walk_frame.handle_apply_event(None)

        y_axis_xpath = './/mapping[@name="LeftY_Axis"][@type="Axis"]'
        x_axis_xpath = './/mapping[@name="LeftX_Axis"][@type="Axis"]'

        self.button_factory.add.assert_has_calls([
            call(y_axis_xpath, self.mapping_entry.get.return_value),
            call(x_axis_xpath, self.mapping_entry.get.return_value),
        ])

    def test_it_handles_entry_clicked_event(self):
        self.remap_walk_frame.handle_entry_clicked(None)
        self.mapping_entry.delete.assert_called_once_with(0, 'end')

    def test_it_handles_entry_changed_event(self):
        event = MagicMock()
        self.remap_walk_frame.handle_entry_changed(event)
        self.mapping_entry.delete.assert_called_once_with(0, 'end')
        self.mapping_entry.insert.assert_called_once_with(0, event.keysym)
