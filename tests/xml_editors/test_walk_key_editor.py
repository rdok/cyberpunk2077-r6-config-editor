import unittest
from unittest.mock import MagicMock, patch

from src.config import Config
from src.xml_editors.walk_key_editor import WalkKeyEditor, XAxis, YAxis
from src.xml_editors.walk_key_editor.walk_key import WalkKey


class TestWalkKeyEditor(unittest.TestCase):

    @patch('src.xml_editors.walk_key_editor.ElementTree')
    def test_delegates_editing_to_its_services(self, element_tree):
        walk_key = MagicMock()
        config = MagicMock(spec=Config)
        filename = config.get_input_user_mappings_path.return_value
        root = element_tree.parse.return_value

        x_axis = MagicMock(spec=XAxis)
        y_axis = MagicMock(spec=YAxis)
        walk_key = MagicMock(spec=WalkKey)

        self.element = WalkKeyEditor(
            config=config,
            x_axis=x_axis,
            y_axis=y_axis,
            walk_key=walk_key,
        )

        self.element.write(walk_key)

        element_tree.parse.assert_called_once_with(filename)
        walk_key.put.assert_called_once_with(root, walk_key)

        x_axis.put_forward.assert_called_once_with(root)
        x_axis.put_back.assert_called_once_with(root)
        x_axis.update_left.assert_called_once_with(root)
        x_axis.update_right.assert_called_once_with(root)

        y_axis.put_left.assert_called_once_with(root)
        y_axis.put_right.assert_called_once_with(root)
        y_axis.update_back.assert_called_once_with(root)
        y_axis.update_forward.assert_called_once_with(root)

        root.write.assert_called_once_with(filename)

    # @patch('src.xml_editors.walk_element.SubElement')
    # def test_creates_y_axis_elements_horizontally(self, sub_element):
    #     root = MagicMock()
    #     left_btn_id = root.find.return_value
    #     right_btn_id = root.find.return_value
    #     root.find.side_effect = [left_btn_id, right_btn_id]
    #
    #     mapping = MagicMock()
    #     mapping.find.side_effect = [None, None]
    #     left_btn = MagicMock()
    #     right_btn = MagicMock()
    #     sub_element.side_effect = [left_btn, right_btn]
    #
    #     self.element.put_y_axis_horizontally(y_mapping=mapping, root=root)
    #
    #     attributes = {'id': left_btn_id, 'val': '0', 'overridableUI': 'left'}
    #     left_btn_call = call(mapping, 'button', attributes)
    #
    #     attributes = {'id': right_btn_id, 'val': '0', 'overridableUI': 'right', }
    #     right_btn_call = call(mapping, 'button', attributes)
    #
    #     sub_element.assert_has_calls([left_btn_call, right_btn_call])
    #     self.assertEqual(left_btn.tail, '\n')
    #     self.assertEqual(right_btn.tail, '\n')
    #
    # @patch('src.xml_editors.walk_element.SubElement')
    # def test_updates_y_axis_elements_horizontally(self, sub_element):
    #     y_axis_mapping = MagicMock()
    #     left_btn = MagicMock()
    #     right_btn = MagicMock()
    #     y_axis_mapping.find.side_effect = [left_btn, right_btn]
    #     sub_element.side_effect = [left_btn, right_btn]
    #
    #     self.element.put_y_axis_horizontally(y_mapping=y_axis_mapping)
    #
    #     attributes = {'id': 'IK_A', 'val': '0', 'overridableUI': 'left'}
    #     left_btn_call = call(y_axis_mapping, 'button', attributes)
    #
    #     attributes = {'id': 'IK_D', 'val': '0', 'overridableUI': 'right', }
    #     right_btn_call = call(y_axis_mapping, 'button', attributes)
    #
    #     left_btn_call.set.assert_called_with('')
    #     sub_element.assert_not_called()
    # @patch('src.xml_editors.walk_element.SubElement')
    # def test_updates_y_axis_elements_for_straight(self, sub_element):
    #     mapping = MagicMock()
    #     self.element.update_y_axis_for_vertical(y_mapping=mapping)
    #
    #     calls = [
    #         call('.//button[@id="IK_W"]'),
    #         call().set('val', '1.4'),
    #         call('.//button[@id="IK_S"]'),
    #         call().set('val', '-1.4'),
    #     ]
    #     mapping.find.assert_has_calls(calls)
    #
    # @patch('src.xml_editors.walk_element.SubElement')
    # def test_creates_walk_key_element(self, sub_element):
    #     x_mappings = MagicMock()
    #     x_mappings.find.return_value = None
    #     y_mappings = MagicMock()
    #     y_mappings.find.return_value = None
    #     x_walk_btn = MagicMock()
    #     y_walk_btn = MagicMock
    #     key = MagicMock()
    #     sub_element.side_effect = [x_walk_btn, y_walk_btn]
    #
    #     self.element.put_walk_key(
    #         key=key, x_mapping=x_mappings, y_mapping=y_mappings
    #     )
    #
    #     self.key_transformer.transform.assert_called_once_with(key)
    #     id = 'IK_{0}'.format(self.key_transformer.transform.return_value)
    #
    #     attributes = {
    #         'id': id, 'val': '0', 'modID': self.config.walk_id.return_value
    #     }
    #
    #     x_call = call(x_mappings, 'button', attributes)
    #     y_call = call(y_mappings, 'button', attributes)
    #     sub_element.assert_has_calls([x_call, y_call])
    #
    #     self.assertEqual(x_walk_btn.tail, '\n')
    #     self.assertEqual(y_walk_btn.tail, '\n')
    #
    # @patch('src.xml_editors.walk_element.SubElement')
    # def test_updates_walk_key_element(self, sub_element):
    #     x_mappings = MagicMock()
    #     y_mappings = MagicMock()
    #     x_walk_btn = MagicMock()
    #     y_walk_btn = MagicMock()
    #     x_mappings.find.return_value = x_walk_btn
    #     y_mappings.find.return_value = y_walk_btn
    #
    #     key = MagicMock()
    #     sub_element.side_effect = [x_walk_btn, y_walk_btn]
    #
    #     self.element.put_walk_key(
    #         key=key, x_mapping=x_mappings, y_mapping=y_mappings
    #     )
    #
    #     self.key_transformer.transform.assert_called_once_with(key)
    #     id = 'IK_{0}'.format(self.key_transformer.transform.return_value)
    #
    #     sub_element.assert_not_called()
    #     x_walk_btn.set.assert_has_calls([call('id', id), call('val', '0')])
    #     y_walk_btn.set.assert_has_calls([call('id', id), call('val', '0')])
