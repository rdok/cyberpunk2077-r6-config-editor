import unittest
from unittest.mock import MagicMock, patch

from src.xml_editors.IDLocators import IDLocators
from src.xml_editors.walk_key_editor import XAxis


class TestXAxis(unittest.TestCase):
    def test_updates_x_axis_forward(self):
        root = MagicMock()
        x_axis_root = root.find.return_value
        id_locators = MagicMock(spec=IDLocators)
        x_axis = XAxis(id_locators=id_locators)

        x_axis.put_forward(root)

        root.find.assert_called_once_with('.//mapping[@name="LeftX_Axis"]')
        xpath = './/button[@overridableUI="forward"]'
        x_axis_root.find.assert_called_once_with(xpath)
        x_axis_root.find.return_value.set.assert_called_once_with('val', '0')

    @patch('src.xml_editors.walk_key_editor.x_axis.SubElement')
    def test_creates_x_axis_forward(self, sub_element):
        root = MagicMock()
        x_axis_root = root.find.return_value
        x_axis_root.find.return_value = None
        id_locators = MagicMock(spec=IDLocators)
        x_axis = XAxis(id_locators=id_locators)

        x_axis.put_forward(root)

        root.find.assert_called_once_with('.//mapping[@name="LeftX_Axis"]')
        xpath = './/button[@overridableUI="forward"]'
        x_axis_root.find.assert_called_once_with(xpath)

        id = id_locators.forward.return_value
        attributes = {'id': id, 'val': '0', 'overridableUI': 'forward'}
        sub_element.assert_called_once_with(x_axis_root, 'button', attributes)

    def test_updates_x_axis_back(self):
        root = MagicMock()
        x_axis_root = root.find.return_value
        back = MagicMock()
        x_axis_root.find.return_value = back
        id_locators = MagicMock(spec=IDLocators)
        x_axis = XAxis(id_locators=id_locators)

        x_axis.put_back(root)

        root.find.assert_called_once_with('.//mapping[@name="LeftX_Axis"]')
        xpath = './/button[@overridableUI="back"]'
        x_axis_root.find.assert_called_once_with(xpath)
        back.set.assert_called_once_with('val', '0')

    @patch('src.xml_editors.walk_key_editor.x_axis.SubElement')
    def test_creates_x_axis_back(self, sub_element):
        root = MagicMock()
        x_axis_root = root.find.return_value
        x_axis_root.find.return_value = None
        id_locators = MagicMock(spec=IDLocators)
        x_axis = XAxis(id_locators=id_locators)

        x_axis.put_back(root)

        root.find.assert_called_once_with('.//mapping[@name="LeftX_Axis"]')
        xpath = './/button[@overridableUI="back"]'
        x_axis_root.find.assert_called_once_with(xpath)

        id = id_locators.back.return_value
        attributes = {'id': id, 'val': '0', 'overridableUI': 'back'}
        sub_element.assert_called_once_with(x_axis_root, 'button', attributes)
