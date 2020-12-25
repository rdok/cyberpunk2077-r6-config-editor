import unittest
from unittest.mock import patch, MagicMock, call

from src.config import Config
from src.transformers.key_transformer import KeyTransformer
from src.xml_editors.walk_key_editor import WalkKey


class TestWalkKey(unittest.TestCase):
    def setUp(self) -> None:
        self.config = MagicMock(Config)
        self.transformer = MagicMock(KeyTransformer)
        self.filename = self.config.get_input_user_mappings_path.return_value
        self.key = MagicMock()
        self.root = MagicMock()

    @patch('src.xml_editors.walk_key_editor.walk_key.ElementTree')
    def test_locates_itself(self, element_tree):
        root = element_tree.parse.return_value
        expected_element = root.find.return_value
        walk_id = self.config.walk_id.return_value

        walk_key = WalkKey(config=self.config, transformer=self.transformer)
        actual_element = walk_key.find()

        element_tree.parse.assert_called_once_with(self.filename)
        path = f'.//mapping[@name="LeftX_Axis"]//button[@modID="{walk_id}"]'
        root.find.assert_called_once_with(path)
        self.assertEqual(expected_element, actual_element)

    @patch('src.xml_editors.walk_key_editor.walk_key.SubElement')
    def test_creates_walk_key_element(self, sub_element):
        x_axis = MagicMock()
        x_axis.find.return_value = None
        y_axis = MagicMock()
        y_axis.find.return_value = None
        self.root.find.side_effect = [x_axis, y_axis]
        x_walk_btn = MagicMock()
        y_walk_btn = MagicMock()
        sub_element.side_effect = [x_walk_btn, y_walk_btn]

        mod_id = self.config.walk_id.return_value

        walk_key = WalkKey(config=self.config, transformer=self.transformer)
        walk_key.put(key=self.key, root=self.root)

        self.transformer.transform.assert_called_once_with(self.key)
        id = 'IK_{0}'.format(self.transformer.transform.return_value)

        attributes = {'id': id, 'val': '0', 'modID': mod_id}
        x_call = call(x_axis, 'button', attributes)
        y_call = call(y_axis, 'button', attributes)
        sub_element.assert_has_calls([x_call, y_call])

        self.assertEqual(x_walk_btn.tail, '\n')
        self.assertEqual(y_walk_btn.tail, '\n')

    @patch('src.xml_editors.walk_key_editor.walk_key.SubElement')
    def test_updates_walk_key_element(self, sub_element):
        x_walk_btn = MagicMock()
        y_walk_btn = MagicMock()
        x_axis = MagicMock()
        x_axis.find.return_value = x_walk_btn
        y_axis = MagicMock()
        y_axis.find.return_value = y_walk_btn
        self.root.find.side_effect = [x_axis, y_axis]
        sub_element.side_effect = [x_walk_btn, y_walk_btn]

        sub_element.side_effect = [x_walk_btn, y_walk_btn]

        walk_key = WalkKey(config=self.config, transformer=self.transformer)
        walk_key.put(key=self.key, root=self.root)

        self.transformer.transform.assert_called_once_with(self.key)
        id = 'IK_{0}'.format(self.transformer.transform.return_value)

        sub_element.assert_not_called()
        x_walk_btn.set.assert_has_calls([call('id', id), call('val', '0')])
        y_walk_btn.set.assert_has_calls([call('id', id), call('val', '0')])
