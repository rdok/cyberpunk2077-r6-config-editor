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
        x_mapping = root.find('.//mapping[@name="LeftX_Axis"]')
        y_mapping = root.find('.//mapping[@name="LeftY_Axis"]')

        self.update_x_horizontal(x_mapping)
        self.put_x_vertical(x_mapping)
        self.put_xik_s(x_mapping)
        self.put_walk_key(walk_key, x_mapping=x_mapping, y_mapping=y_mapping)

        root.write(filename)

    def update_xik_d_value(self, root: ElementTree):
        pass

    def put_xik_s(self, root: ElementTree):
        pass

    def put_walk_key(self, key, x_mapping: ElementTree, y_mapping: ElementTree):
        id = 'IK_{0}'.format(self.key_transformer.transform(key))
        mod_id = self.config.walk_id()
        attributes = {'id': id, 'val': '0', 'modID': mod_id}

        x_element = x_mapping.find(f'.//button[@modID="{mod_id}"]')
        if x_element is None:
            x_element = SubElement(x_mapping, 'button', attributes)
            x_element.tail = '\n'
        else:
            x_element.set('id', id)
            x_element.set('val', '0')

        y_element = y_mapping.find(f'.//button[@modID="{mod_id}"]')
        if y_element is None:
            y_element = SubElement(y_mapping, 'button', attributes)
            y_element.tail = '\n'
        else:
            y_element.set('id', id)
            y_element.set('val', '0')

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
