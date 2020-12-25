import unittest
from unittest.mock import MagicMock, patch

from src.xml_editors.IDLocators import IDLocators
from src.xml_editors.walk_key_editor import XAxisBack


class TestXAxisBack(unittest.TestCase):
    def setUp(self) -> None:
        self.root = MagicMock()
        self.x_axis = self.root.find.return_value
        self.back = self.x_axis.find.return_value
        self.id_locators = MagicMock(spec=IDLocators)

    def test_updates_x_axis_back(self):
        self.back = MagicMock()
        self.x_axis.find.return_value = self.back
        self.x_axis_back = XAxisBack(id_locators=self.id_locators)
        self.x_axis_back.put(self.root)

        self.root.find.assert_called_once_with('.//mapping[@name="LeftX_Axis"]')
        xpath = './/button[@overridableUI="back"]'
        self.x_axis.find.assert_called_once_with(xpath)
        self.back.set.assert_called_once_with('val', '0')

    @patch('src.xml_editors.walk_key_editor.x_axis_back.SubElement')
    def test_creates_x_axis_back(self, sub_element):
        self.back = None
        self.x_axis.find.return_value = self.back
        x_axis_back = XAxisBack(id_locators=self.id_locators)
        x_axis_back.put(self.root)

        self.root.find.assert_called_once_with('.//mapping[@name="LeftX_Axis"]')
        self.x_axis.find.assert_called_once_with('.//button[@overridableUI="back"]')

        id = self.id_locators.back.return_value
        attributes = {'id': id, 'val': '0', 'overridableUI': 'back'}
        sub_element.assert_called_once_with(self.x_axis, 'button', attributes)
