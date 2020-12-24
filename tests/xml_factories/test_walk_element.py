import unittest
from unittest.mock import MagicMock, patch, call

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

    @patch('src.xml_factories.walk_element.ElementTree')
    def test_it_should_locate_itself(self, element_tree):
        filename = self.config.get_input_user_mappings_path.return_value
        root = element_tree.parse.return_value
        expected_element = root.find.return_value
        walk_id = self.config.walk_id.return_value

        actual_element = self.element.find()

        element_tree.parse.assert_called_once_with(filename)
        root.find.assert_called_once_with(f'.//mapping[@modID="{walk_id}"]')
        self.assertEqual(expected_element, actual_element)

    @patch('src.xml_factories.walk_element.ElementTree')
    def test_it_should_save_itself(self, element_tree):
        root = element_tree.parse.return_value
        x_mapping = root.find.return_value

        self.element.update_x_side = MagicMock()
        self.element.update_or_create_x_straight = MagicMock()
        self.element.update_or_create_xik_s = MagicMock()
        self.element.update_or_create_xik_walk_key = MagicMock()
        filename = self.config.get_input_user_mappings_path.return_value
        new_walk_key = MagicMock()

        self.element.write(new_walk_key)

        self.element.update_x_side.assert_called_once_with(x_mapping)
        self.element.update_or_create_x_straight.assert_called_once_with(x_mapping)
        self.element.update_or_create_xik_s.assert_called_once_with(x_mapping)
        self.element.update_or_create_xik_walk_key.assert_called_once_with(
            x_mapping, new_walk_key
        )
        root.write.assert_called_once_with(filename)

    def test_it_should_update_horizontal_side_movement(self):
        horizontal_mapping = MagicMock()
        self.element.update_x_side(horizontal_mapping)

        calls = [call('//button[@id="IK_A"]'), call('//button[@id="IK_D"]')]
        horizontal_mapping.find.assert_has_calls(calls)

        calls = [call('val', '-1.4'), call('val', '1.4'), ]
        horizontal_mapping.find.return_value.set.assert_has_calls(calls)

    @patch('src.xml_factories.walk_element.SubElement')
    def test_it_should_create_horizontal_straight_movement(self, sub_element):
        horizontal_mapping = MagicMock()
        forward_btn = MagicMock()
        back_btn = MagicMock()
        sub_element.side_effect = [forward_btn, back_btn]
        self.element \
            .update_or_create_x_straight(horizontal_mapping=horizontal_mapping)

        forward_btn_call = call(horizontal_mapping, 'button', {
            'id': 'IK_W',
            'val': '0',
            'overridableUI': 'forward',
            'modID': self.config.walk_id.return_value
        })

        back_btn_call = call(horizontal_mapping, 'button', {
            'id': 'IK_S',
            'val': '0',
            'overridableUI': 'back',
            'modID': self.config.walk_id.return_value
        })

        sub_element.assert_has_calls([forward_btn_call, back_btn_call])
        self.assertEqual(forward_btn.tail, '\n')
        self.assertEqual(back_btn.tail, '\n')
