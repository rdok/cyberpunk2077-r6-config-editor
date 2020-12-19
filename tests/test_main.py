import os
from types import SimpleNamespace
from unittest.mock import patch, call, MagicMock
from xml.etree import ElementTree

import src
from src.main import main


@patch.object(ElementTree, 'parse')
@patch('src.main.SubElement')
def test_it_adds_slow_forward_walk_button(sub_element, element_tree_parse):
    tree = element_tree_parse.return_value
    y_axis_movement_el = MagicMock()
    tree.find = MagicMock()
    tree.find.side_effect = [y_axis_movement_el, None]

    args = SimpleNamespace(input_user_mappings_path='mocked_input_user_mappings_path')
    src.main.main(args)

    src_name = os.path.dirname(__file__).rstrip('tests') + 'src'
    filename = os.path.join(src_name, 'mocked_input_user_mappings_path')

    element_tree_parse.assert_called_once_with(filename)

    element_tree_parse.assert_called_once_with(filename)
    y_axis_mappings_xpath = './/mapping[@name="LeftY_Axis"][@type="Axis"]'
    slow_walk_xpath = '{0}{1}'.format(
        y_axis_mappings_xpath,
        '//button[@id="IK_CapsLock"][@val="0"][@overridableUI="forward"]'
    )

    calls = [call(y_axis_mappings_xpath), call(slow_walk_xpath)]
    tree.find.assert_has_calls(calls)
    sub_element.assert_called_once_with(
        y_axis_movement_el,
        'button',
        {'id': 'IK_CapsLock', 'val': '0', 'overridableUI': 'forward'}
    )

    tree.write.assert_called_once_with(filename)


@patch.object(ElementTree, 'parse')
@patch('src.main.SubElement')
def test_should_not_duplicate_slow_forward_walk_button(sub_element, element_tree_parse):
    tree = element_tree_parse.return_value
    tree.find.return_value = [MagicMock(), None]

    args = SimpleNamespace(input_user_mappings_path='mocked_input_user_mappings_path')
    src.main.main(args)

    sub_element.assert_not_called()
    tree.write.assert_not_called()
