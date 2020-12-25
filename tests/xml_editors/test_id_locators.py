import unittest
from unittest.mock import MagicMock

from src.xml_editors.IDLocators import IDLocators


class TestIDLocators(unittest.TestCase):
    def setUp(self) -> None:
        self.id_locators = IDLocators()
        self.root = MagicMock()
        self.element = self.root.find.return_value
        self.expected = self.element.get.return_value

    def test_locates_back_id(self):
        actual = self.id_locators.back(self.root)

        xpath = './/mapping[@name="LeftY_Axis"]//button[@overridableUI="back"]'
        self.root.find.assert_called_once_with(xpath)
        self.root.find.return_value.get.assert_called_once_with('id')
        self.assertEqual(self.expected, actual)

    def test_locates_forward_id(self):
        actual = self.id_locators.forward(self.root)

        xpath = './/mapping[@name="LeftY_Axis"]//button[@overridableUI="forward"]'
        self.root.find.assert_called_once_with(xpath)
        self.root.find.return_value.get.assert_called_once_with('id')
        self.assertEqual(self.expected, actual)

    def test_locates_left_id(self):
        actual = self.id_locators.left(self.root)

        xpath = './/mapping[@name="LeftX_Axis"]//button[@overridableUI="left"]'
        self.root.find.assert_called_once_with(xpath)
        self.root.find.return_value.get.assert_called_once_with('id')
        self.assertEqual(self.expected, actual)

    def test_locates_right_id(self):
        actual = self.id_locators.right(self.root)

        xpath = './/mapping[@name="LeftX_Axis"]//button[@overridableUI="right"]'
        self.root.find.assert_called_once_with(xpath)
        self.root.find.return_value.get.assert_called_once_with('id')
        self.assertEqual(self.expected, actual)
