import unittest
from unittest.mock import MagicMock, patch

from src.xml_editors.IDLocators import IDLocators
from src.xml_editors.walk_key_editor import XAxisForward


class TestXAxisForward(unittest.TestCase):
    def setUp(self) -> None:
        self.root = MagicMock()
        self.x_axis = self.root.find.return_value
        self.forward = self.x_axis.find.return_value
        self.id_locators = MagicMock(spec=IDLocators)

    def test_updates_x_axis_forward(self):
        self.forward = MagicMock()
        self.x_axis.find.return_value = self.forward
        self.x_axis_forward = XAxisForward(id_locators=self.id_locators)
        self.x_axis_forward.put(self.root)

        self.root.find.assert_called_once_with('.//mapping[@name="LeftX_Axis"]')
        xpath = './/button[@overridableUI="forward"]'
        self.x_axis.find.assert_called_once_with(xpath)
        self.forward.set.assert_called_once_with('val', '0')

    @patch('src.xml_editors.walk_key_editor.x_axis_forward.SubElement')
    def test_creates_x_axis_forward(self, sub_element):
        self.forward = None
        self.x_axis.find.return_value = self.forward
        x_axis_forward = XAxisForward(id_locators=self.id_locators)
        x_axis_forward.put(self.root)

        self.root.find.assert_called_once_with('.//mapping[@name="LeftX_Axis"]')
        self.x_axis.find.assert_called_once_with('.//button[@overridableUI="forward"]')

        id = self.id_locators.forward.return_value
        attributes = {'id': id, 'val': '0', 'overridableUI': 'forward'}
        sub_element.assert_called_once_with(self.x_axis, 'button', attributes)
