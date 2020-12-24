from xml.etree import ElementTree

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

        self.update_xik(root)
        self.update_or_create_xik_w(root)
        self.update_or_create_xik_s(root)
        self.update_or_create_xik_walk_key(root, walk_key)

        root.write(filename)

    def update_xik(self, root: ElementTree):
        ik_a_element = root.find('.//mapping[@id="IK_A"]')
        ik_d_element = root.find('.//mapping[@id="IK_D"]')
        ik_a_element.set('val', '-1.4')
        ik_d_element.set('val', '1.4')

    def update_xik_d_value(self, root: ElementTree):
        pass

    def update_or_create_xik_s(self, root: ElementTree):
        pass

    def update_or_create_xik_walk_key(self, root: ElementTree, key):
        pass

    def update_or_create_xik_w(self, root: ElementTree):
        pass
