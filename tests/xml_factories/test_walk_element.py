import unittest
from unittest.mock import MagicMock, patch, call
from xml.etree import ElementTree

from src.config import Config
from src.transformers.key_transformer import KeyTransformer
from src.xml_factories.walk_element import WalkElement


class TestWalkElement(unittest.TestCase):

    def setUp(self) -> None:
        self.config = MagicMock(spec=Config)
        self.key_transformer = MagicMock(spec=KeyTransformer)
        self.element = WalkElement(
            config=self.config, key_transformer=self.key_transformer
        )
        self.root = MagicMock(spec=ElementTree)
        self.root.find = MagicMock()

    @patch('src.xml_factories.walk_element.ElementTree')
    def test_it_should_locate_itself(self, element_tree):
        filename = self.config.get_input_user_mappings_path.return_value
        root = element_tree.parse.return_value
        expected_element = root.find.return_value
        moid_id = self.config.walk_id.return_value

        actual_element = self.element.find()

        element_tree.parse.assert_called_once_with(filename)
        root.find.assert_called_once_with(f'.//mapping[@modID="{moid_id}"]')
        self.assertEqual(expected_element, actual_element)

    @patch('src.xml_factories.walk_element.ElementTree')
    def test_it_should_save_itself(self, element_tree):
        root = element_tree.parse.return_value
        self.element.update_xik = MagicMock()
        self.element.update_or_create_xik_w = MagicMock()
        self.element.update_or_create_xik_s = MagicMock()
        self.element.update_or_create_xik_walk_key = MagicMock()
        filename = self.config.get_input_user_mappings_path.return_value
        new_walk_key = MagicMock()

        self.element.write(new_walk_key)

        self.element.update_xik.assert_called_once_with(root)
        self.element.update_or_create_xik_w.assert_called_once_with(root)
        self.element.update_or_create_xik_s.assert_called_once_with(root)
        self.element.update_or_create_xik_walk_key \
            .assert_called_once_with(root, new_walk_key)
        root.write.assert_called_once_with(filename)

    def test_it_should_update_xik_side_movement(self):
        self.element.update_xik(root=self.root)

        calls = [call('.//mapping[@id="IK_A"]'), call('.//mapping[@id="IK_D"]')]
        self.root.find.assert_has_calls(calls)

        calls = [call('val', '-1.4'), call('val', '1.4'), ]
        self.root.find.return_value.set.assert_has_calls(calls)

    # @patch('src.xml_factories.walk_element.SubElement')
    # def test_it_should_create_xik_straightforward_elements(self, sub_element):
    #     self.element.update_or_create_xik_w(root=self.root)
    #
    #     self.root.find.assert_called_once_with('.//mapping[@id="IK_W"]')
    #     self.root.find.return_value = None
    #     sub_element.assert_called_once_with(mappings_element, 'button', {
    #         'id': 'IK_transformedkey', 'val': '0',
    #         'modID': config.walk_id.return_value
    #     })
