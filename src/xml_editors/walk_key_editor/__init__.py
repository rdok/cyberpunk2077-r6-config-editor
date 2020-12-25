from xml.etree import ElementTree

from src.config import Config
from src.xml_editors.walk_key_editor.walk_key import WalkKey
from src.xml_editors.walk_key_editor.x_axis import XAxis
from src.xml_editors.walk_key_editor.y_axis import YAxis


class WalkKeyEditor:
    def __init__(
        self,
        config: Config,
        x_axis: XAxis,
        y_axis: YAxis,
        walk_key: WalkKey
    ):
        self.y_axis = y_axis
        self.config = config
        self.x_axis = x_axis
        self.walk_key = walk_key

    def write(self, walk_key: str):
        filename = self.config.get_input_user_mappings_path()
        root = ElementTree.parse(filename)

        self.walk_key.put(root, walk_key)
        self.x_axis.put_forward(root)
        self.x_axis.put_back(root)
        self.x_axis.update_left(root)
        self.x_axis.update_right(root)

        self.y_axis.put_left(root)
        self.y_axis.put_right(root)
        self.y_axis.update_back(root)
        self.y_axis.update_forward(root)

        root.write(filename)

    # def update_y_axis_for_vertical(self, y_mapping: ElementTree):
    #     forward = y_mapping.find('.//button[@overridableUI="forward"]')
    #     forward.set('val', '1.4')
    #
    #     back = y_mapping.find('.//button[@overridableUI="back"]')
    #     back.set('val', '-1.4')
    #
    # def locate_back_id(self, root: ElementTree):
    #     xpath = './/bindings//mapping[{0}]//button[{1}]' \
    #         .format('@name="LeftY_Axis"', '@overridableUI="back"')
    #     return root.find(xpath)
    #
    # def put_y_axis_horizontally(
    #     self, y_mapping: ElementTree, left_id, right_id
    # ):
    #     left_btn = y_mapping.find('.//button[@overridableUI="left"]')
    #
    #     if left_btn is None:
    #         attr = {'id': left_id, 'val': '0', 'overridableUI': 'left'}
    #         left_btn = SubElement(y_mapping, 'button', attr)
    #         left_btn.tail = '\n'
    #     # else:
    #     #     left_btn.set('val', '0')
    #
    #     right = y_mapping.find('.//button[@overridableUI="right"]')
    #     if right is None:
    #         attr = {'id': right_id, 'val': '0', 'overridableUI': 'right'}
    #         back_btn = SubElement(y_mapping, 'button', attr)
    #         back_btn.tail = '\n'
    #     # else:
    #     #     back.set('val', '0')
    #     #     back.set('override', '0')
    #
