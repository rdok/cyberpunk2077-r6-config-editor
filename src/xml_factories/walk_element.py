from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

from src.config import Config
from src.transformers.key_transformer import KeyTransformer


class WalkElement:
    def __init__(self, config: Config, key_transformer: KeyTransformer):
        self.key_transformer = key_transformer
        self.config = config

    def find(self):
        filename = self.config.get_input_user_mappings_path()
        root = ElementTree.parse(filename)
        mod_id = self.config.walk_id()
        return root.find(f'.//mapping[@modID="{mod_id}"]')

    def write(self, walk_key):
        filename = self.config.get_input_user_mappings_path()
        root = ElementTree.parse(filename)
        horizontal_mapping = root.find('.//mapping[@name="LeftX_Axis"]')

        self.update_x_side(horizontal_mapping)
        self.update_or_create_x_straight(horizontal_mapping)
        self.update_or_create_xik_s(horizontal_mapping)
        self.update_or_create_xik_walk_key(horizontal_mapping, walk_key)

        root.write(filename)

    def update_x_side(self, horizontal_mapping: ElementTree):
        left_move = horizontal_mapping.find('.//button[@id="IK_A"]')
        right_move = horizontal_mapping.find('.//button[@id="IK_D"]')
        left_move.set('val', '-1.4')
        right_move.set('val', '1.4')

    def update_xik_d_value(self, root: ElementTree):
        pass

    def update_or_create_xik_s(self, root: ElementTree):
        pass

    def update_or_create_xik_walk_key(self, root: ElementTree, key):
        pass

    def update_or_create_x_straight(self, horizontal_mapping: ElementTree):
        should_create = horizontal_mapping.find('.//button[@id="IK_W"]') is None
        if should_create:
            forward_btn = SubElement(horizontal_mapping, 'button', {
                'id': 'IK_W',
                'val': '0',
                'overridableUI': 'forward',
            })
            forward_btn.tail = '\n'

        should_create = horizontal_mapping.find('.//button[@id="IK_S"]') is None
        if should_create:
            back_btn = SubElement(horizontal_mapping, 'button', {
                'id': 'IK_S',
                'val': '0',
                'overridableUI': 'back',
            })
            back_btn.tail = '\n'
