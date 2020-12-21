from xml.etree.ElementTree import SubElement
from xml.etree import ElementTree

from src.config import Config
from src.transformers.key_transformer import KeyTransformer


class ButtonFactory:
    key_transformer: KeyTransformer
    config: Config

    def __init__(self, key_transformer: KeyTransformer, config: Config):
        self.config = config
        self.key_transformer = key_transformer

    def add(self, mappings_element_xpath, mapping_keymap):
        filename = self.config.get_input_user_mappings_path()
        root = ElementTree.parse(filename)

        existing_btn_el_xpath = '{0}//button[@modID="{1}"]'.format(
            mappings_element_xpath, self.config.get_walk_id())
        mappings_element = root.find(mappings_element_xpath)
        walk_btn_elements = root.findall(existing_btn_el_xpath)

        for walk_btn_el in walk_btn_elements:
            mappings_element.remove(walk_btn_el)

        id = 'IK_' + self.key_transformer.transform(mapping_keymap)
        attributes = {'id': id, 'val': '0', 'modID': self.config.get_walk_id()}
        element = SubElement(mappings_element, 'button', attributes)
        element.tail = '\n'

        root.write(filename)
