from xml.etree.ElementTree import SubElement

from src.transformers.key_transformer import KeyTransformer


class Button:
    def __init__(self, key_transformer: KeyTransformer):
        self.key_transformer = key_transformer

    def append_to(self, mappings_xpath, element_tree, mapping_entry):
        walk_overridable_ui = 'slowWalk'
        id = 'IK_' + self.key_transformer.transform(mapping_entry)

        btn_el_xpath = \
            '{0}//button[@id="{1}"][@val="0"][@overridableUI="{2}"]'.format(
                id,
                mapping_entry,
                walk_overridable_ui
            )
        slow_walk_button_element = element_tree.find(
            btn_el_xpath
        )

        if slow_walk_button_element is not None:
            return False

        attributes = {
            'id': id,
            'val': '0',
            'overridableUI': walk_overridable_ui
        }
        mappings_element = element_tree.find(mappings_xpath)
        element = SubElement(mappings_element, 'button', attributes)
        element.tail = '\n'

        return True