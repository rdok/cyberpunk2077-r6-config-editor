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

        self.update_x_horizontal(horizontal_mapping)
        self.put_x_vertical(horizontal_mapping)
        self.put_xik_s(horizontal_mapping)
        self.put_walk_key(root, walk_key)

        root.write(filename)

    def update_xik_d_value(self, root: ElementTree):
        pass

    def put_xik_s(self, root: ElementTree):
        pass

    def put_walk_key(self, key, x_mappings: ElementTree, y_mappings: ElementTree):
        id = 'IK_{0}'.format(self.key_transformer.transform(key))
        mod_id = self.config.walk_id()
        attributes = {'id': id, 'val': '0', 'modID': mod_id}

        x_element = SubElement(x_mappings, 'button', attributes)
        x_element.tail = '\n'

        y_element = SubElement(y_mappings, 'button', attributes)
        y_element.tail = '\n'

    def update_x_horizontal(self, x_mappings: ElementTree):
        left_move = x_mappings.find('.//button[@id="IK_A"]')
        right_move = x_mappings.find('.//button[@id="IK_D"]')
        left_move.set('val', '-1.4')
        right_move.set('val', '1.4')

    def put_x_vertical(self, x_mappings: ElementTree):
        forward = x_mappings.find('.//button[@id="IK_W"]')
        if forward is None:
            forward_btn = SubElement(x_mappings, 'button', {
                'id': 'IK_W',
                'val': '0',
                'overridableUI': 'forward',
            })
            forward_btn.tail = '\n'
        else:
            forward.set('val', '0')

        back = x_mappings.find('.//button[@id="IK_S"]')
        if back is None:
            back_btn = SubElement(x_mappings, 'button', {
                'id': 'IK_S',
                'val': '0',
                'overridableUI': 'back',
            })
            back_btn.tail = '\n'
        else:
            back.set('val', '0')
