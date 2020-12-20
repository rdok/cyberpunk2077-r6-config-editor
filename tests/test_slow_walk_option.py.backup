import os
from types import SimpleNamespace
from unittest.mock import patch, MagicMock, call
from xml.etree import ElementTree

import src
from src.main import main
from src.slow_walk_element import SlowWalkElement


@patch.object(ElementTree, 'parse')
def test_it_maps_slow_walk_buttons(element_tree_parse):
    tree = element_tree_parse.return_value
    slow_walk_element = MagicMock(spec=SlowWalkElement)
    slow_walk_element.write = MagicMock()

    args = SimpleNamespace(input_user_mappings_path='input_user_mappings_path')
    dependencies = {SlowWalkElement.__name__: slow_walk_element}
    src.main.main(args, dependencies)

    src_name = os.path.dirname(__file__).rstrip('tests') + 'src'
    filename = os.path.join(src_name, 'input_user_mappings_path')

    element_tree_parse.assert_called_once_with(filename)

    slow_walk_element.append_to.assert_has_calls([
        call('.//mapping[@name="LeftY_Axis"][@type="Axis"]', tree),
        call('.//mapping[@name="LeftX_Axis"][@type="Axis"]', tree)
    ])

    tree.write.assert_called_once_with(filename)
