import unittest
from unittest.mock import MagicMock, patch

from src.xml_editors.IDLocators import IDLocators
from src.xml_editors.walk_key_editor.y_axis import YAxis


class TestYAxis(unittest.TestCase):
    def test_updates_y_axis_forward(self):
        root = MagicMock()
        y_axis_root = root.find.return_value
        id_locators = MagicMock(spec=IDLocators)
        y_axis = YAxis(id_locators=id_locators)

        y_axis.update_forward(root)

        root.find.assert_called_once_with('.//mapping[@name="LeftY_Axis"]')
        xpath = './/button[@overridableUI="forward"]'
        y_axis_root.find.assert_called_once_with(xpath)
        y_axis_root.find.return_value.set.assert_called_once_with('val', '1.4')

    def test_updates_y_axis_back(self):
        root = MagicMock()
        y_axis_root = root.find.return_value
        id_locators = MagicMock(spec=IDLocators)
        y_axis = YAxis(id_locators=id_locators)

        y_axis.update_back(root)

        root.find.assert_called_once_with('.//mapping[@name="LeftY_Axis"]')
        xpath = './/button[@overridableUI="back"]'
        y_axis_root.find.assert_called_once_with(xpath)
        y_axis_root.find.return_value.set. \
            assert_called_once_with('val', '-1.4')

    @patch('src.xml_editors.walk_key_editor.y_axis.SubElement')
    def test_creates_y_axis_right(self, sub_element):
        root = MagicMock()
        y_axis_root = root.find.return_value
        y_axis_root.find.return_value = None
        id_locators = MagicMock(spec=IDLocators)
        y_axis = YAxis(id_locators=id_locators)

        y_axis.put_right(root)

        root.find.assert_called_once_with('.//mapping[@name="LeftY_Axis"]')
        xpath = './/button[@overridableUI="right"]'
        y_axis_root.find.assert_called_once_with(xpath)

        id = id_locators.right.return_value
        attributes = {'id': id, 'val': '0', 'overridableUI': 'right'}
        sub_element.assert_called_once_with(y_axis_root, 'button', attributes)
        self.assertEqual('\n', sub_element.return_value.tail)

    def test_updates_y_axis_right(self):
        root = MagicMock()
        y_axis_root = root.find.return_value
        right = MagicMock()
        y_axis_root.find.return_value = right
        id_locators = MagicMock(spec=IDLocators)
        y_axis = YAxis(id_locators=id_locators)

        y_axis.put_right(root)

        root.find.assert_called_once_with('.//mapping[@name="LeftY_Axis"]')
        xpath = './/button[@overridableUI="right"]'
        y_axis_root.find.assert_called_once_with(xpath)
        right.set.assert_called_once_with('val', '0')

    @patch('src.xml_editors.walk_key_editor.y_axis.SubElement')
    def test_creates_y_axis_left(self, sub_element):
        root = MagicMock()
        y_axis_root = root.find.return_value
        y_axis_root.find.return_value = None
        id_locators = MagicMock(spec=IDLocators)
        y_axis = YAxis(id_locators=id_locators)

        y_axis.put_left(root)

        root.find.assert_called_once_with('.//mapping[@name="LeftY_Axis"]')
        xpath = './/button[@overridableUI="left"]'
        y_axis_root.find.assert_called_once_with(xpath)

        id = id_locators.left.return_value
        attributes = {'id': id, 'val': '0', 'overridableUI': 'left'}
        sub_element.assert_called_once_with(y_axis_root, 'button', attributes)
        self.assertEqual('\n', sub_element.return_value.tail)

    def test_updates_y_axis_left(self):
        root = MagicMock()
        y_axis_root = root.find.return_value
        left = MagicMock()
        y_axis_root.find.return_value = left
        id_locators = MagicMock(spec=IDLocators)
        y_axis = YAxis(id_locators=id_locators)

        y_axis.put_left(root)

        root.find.assert_called_once_with('.//mapping[@name="LeftY_Axis"]')
        xpath = './/button[@overridableUI="left"]'
        y_axis_root.find.assert_called_once_with(xpath)
        left.set.assert_called_once_with('val', '0')
