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
        x_mapping = MagicMock()
        y_mapping = MagicMock()
        root.find.side_effect = [x_mapping, y_mapping]

        self.element.update_x_horizontal = MagicMock()
        self.element.put_x_vertical = MagicMock()
        self.element.put_xik_s = MagicMock()
        self.element.put_walk_key = MagicMock()
        filename = self.config.get_input_user_mappings_path.return_value
        walk_key = MagicMock()

        self.element.write(walk_key)

        self.element.update_x_horizontal.assert_called_once_with(x_mapping)
        self.element.put_x_vertical.assert_called_once_with(x_mapping)
        self.element.put_xik_s.assert_called_once_with(x_mapping)
        self.element.put_walk_key.assert_called_once_with(
            walk_key, x_mapping=x_mapping, y_mapping=y_mapping
        )
        root.write.assert_called_once_with(filename)

    def test_it_should_update_horizontal_side_movement(self):
        horizontal_mapping = MagicMock()
        self.element.update_x_horizontal(horizontal_mapping)

        calls = [call('.//button[@id="IK_A"]'), call('.//button[@id="IK_D"]')]
        horizontal_mapping.find.assert_has_calls(calls)

        calls = [call('val', '-1.4'), call('val', '1.4'), ]
        horizontal_mapping.find.return_value.set.assert_has_calls(calls)

    @patch('src.xml_factories.walk_element.SubElement')
    def test_it_should_create_horizontal_straight_movement(self, sub_element):
        mapping = MagicMock()
        mapping.find.side_effect = [None, None]
        forward_btn = MagicMock()
        back_btn = MagicMock()
        sub_element.side_effect = [forward_btn, back_btn]

        self.element.put_x_vertical(x_mappings=mapping)

        attributes = {'id': 'IK_W', 'val': '0', 'overridableUI': 'forward'}
        forward_btn_call = call(mapping, 'button', attributes)

        attributes = {'id': 'IK_S', 'val': '0', 'overridableUI': 'back', }
        back_btn_call = call(mapping, 'button', attributes)

        sub_element.assert_has_calls([forward_btn_call, back_btn_call])
        self.assertEqual(forward_btn.tail, '\n')
        self.assertEqual(back_btn.tail, '\n')

    @patch('src.xml_factories.walk_element.SubElement')
    def test_it_should_update_horizontal_straight_movement(self, sub_element):
        mapping = MagicMock()
        mapping.find.return_value.side_effect = [True, True]
        self.element.put_x_vertical(x_mappings=mapping)

        calls = [
            call('.//button[@id="IK_W"]'),
            call().set('val', '0'),
            call('.//button[@id="IK_S"]'),
            call().set('val', '0'),
        ]
        mapping.find.assert_has_calls(calls)

    @patch('src.xml_factories.walk_element.SubElement')
    def test_it_should_create_walk_key_element(self, sub_element):
        x_mappings = MagicMock()
        x_mappings.find.return_value = None
        y_mappings = MagicMock()
        y_mappings.find.return_value = None
        x_walk_btn = MagicMock()
        y_walk_btn = MagicMock
        key = MagicMock()
        sub_element.side_effect = [x_walk_btn, y_walk_btn]

        self.element.put_walk_key(
            key=key, x_mapping=x_mappings, y_mapping=y_mappings
        )

        self.key_transformer.transform.assert_called_once_with(key)
        id = 'IK_{0}'.format(self.key_transformer.transform.return_value)

        attributes = {
            'id': id, 'val': '0', 'modID': self.config.walk_id.return_value
        }

        x_call = call(x_mappings, 'button', attributes)
        y_call = call(y_mappings, 'button', attributes)
        sub_element.assert_has_calls([x_call, y_call])

        self.assertEqual(x_walk_btn.tail, '\n')
        self.assertEqual(y_walk_btn.tail, '\n')

    @patch('src.xml_factories.walk_element.SubElement')
    def test_it_should_update_walk_key_element(self, sub_element):
        x_mappings = MagicMock()
        y_mappings = MagicMock()
        x_walk_btn = MagicMock()
        y_walk_btn = MagicMock()
        x_mappings.find.return_value = x_walk_btn
        y_mappings.find.return_value = y_walk_btn

        key = MagicMock()
        sub_element.side_effect = [x_walk_btn, y_walk_btn]

        self.element.put_walk_key(
            key=key, x_mapping=x_mappings, y_mapping=y_mappings
        )

        self.key_transformer.transform.assert_called_once_with(key)
        id = 'IK_{0}'.format(self.key_transformer.transform.return_value)

        sub_element.assert_not_called()
        x_walk_btn.set.assert_has_calls([call('id', id), call('val', '0')])
        y_walk_btn.set.assert_has_calls([call('id', id), call('val', '0')])
