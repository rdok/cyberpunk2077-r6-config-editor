import unittest
from unittest.mock import MagicMock, patch

from src.config import Config
from src.xml_editors.walk_key_editor import WalkKeyEditor, XAxis, YAxis
from src.xml_editors.walk_key_editor.walk_key import WalkKey


class TestWalkKeyEditor(unittest.TestCase):

    @patch('src.xml_editors.walk_key_editor.ElementTree')
    def test_delegates_editing_to_its_services(self, element_tree):
        config = MagicMock(spec=Config)
        filename = config.get_input_user_mappings_path.return_value
        root = element_tree.parse.return_value

        x_axis = MagicMock(spec=XAxis)
        y_axis = MagicMock(spec=YAxis)
        walk_key = MagicMock(spec=WalkKey)
        key = MagicMock()

        self.element = WalkKeyEditor(
            config=config,
            x_axis=x_axis,
            y_axis=y_axis,
            walk_key=walk_key,
        )

        self.element.write(key)

        element_tree.parse.assert_called_once_with(filename)
        walk_key.put.assert_called_once_with(key=key, root=root)

        x_axis.put_forward.assert_called_once_with(root)
        x_axis.put_back.assert_called_once_with(root)
        x_axis.update_left.assert_called_once_with(root)
        x_axis.update_right.assert_called_once_with(root)

        y_axis.put_left.assert_called_once_with(root)
        y_axis.put_right.assert_called_once_with(root)
        y_axis.update_back.assert_called_once_with(root)
        y_axis.update_forward.assert_called_once_with(root)

        root.write.assert_called_once_with(filename)

