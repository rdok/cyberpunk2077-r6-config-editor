import os
from types import SimpleNamespace
from unittest.mock import patch
from xml.etree import ElementTree

import pytest

import src
from src.main import main


@patch.object(ElementTree, 'parse')
@patch('src.main.SubElement')
def test_it_adds_forward_walk_button(sub_element, element_tree_parse):
    tree = element_tree_parse.return_value
    y_axis_movement_el = tree.find.return_value

    args = SimpleNamespace(input_user_mappings_path='mocked_input_user_mappings_path')
    src.main.main(args)

    src_name = os.path.dirname(__file__).rstrip('tests') + 'src'
    filename = os.path.join(src_name, 'mocked_input_user_mappings_path')

    element_tree_parse.assert_called_once_with(filename)
    tree.find.assert_called_once_with('.//mapping[@name="LeftY_Axis"][@type="Axis"]')
    sub_element.assert_called_once_with(
        y_axis_movement_el,
        'button',
        {'id': 'IK_CapsLock', 'val': '0', 'overridableUI': 'forward'}
    )

    tree.write.assert_called_once_with(filename)


@pytest.mark.skip(reason="TODO")
def test_it_does_not_add_duplicate_forward_walk_button():
    assert 1 == 0
