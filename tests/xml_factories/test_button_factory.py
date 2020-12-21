import unittest
from unittest.mock import patch, MagicMock

from src.config import Config
from src.transformers.key_transformer import KeyTransformer
from src.xml_factories.button_factory import ButtonFactory

key_transformer: KeyTransformer = MagicMock(spec=KeyTransformer)
mappings_element = MagicMock()
config: Config = MagicMock(spec=Config)
mappings_xpath = MagicMock()
btn_xpath = '{0}//button[@modID="{1}"]'.format(
    mappings_xpath, config.get_walk_id()
)


class TestButtonFactory(unittest.TestCase):
    @patch('src.xml_factories.button_factory.SubElement')
    @patch('src.xml_factories.button_factory.ElementTree')
    def test_it_remaps_walk_buttons(self, element_tree, sub_element):
        root = element_tree.parse.return_value
        root.findall.return_value = []
        root.find.return_value = mappings_element
        mapping_key = 'mockKey'
        key_transformer.transform.return_value = 'transformedkey'
        button_factory = ButtonFactory(
            config=config, key_transformer=key_transformer)
        button_factory.add(mappings_xpath, mapping_key)

        root.find.assert_called_once_with(mappings_xpath)
        sub_element.assert_called_once_with(mappings_element, 'button', {
            'id': 'IK_transformedkey', 'val': '0.2',
            'modID': config.get_walk_id.return_value
        })

        root.remove.assert_not_called()
        root.write.assert_called_with(config.get_input_user_mappings_path())
        self.assertEqual(sub_element.return_value.tail, '\n')

    @patch('src.xml_factories.button_factory.SubElement')
    @patch('src.xml_factories.button_factory.ElementTree')
    def test_it_should_replace_existing_walk_buttons(
            self, element_tree, sub_element):
        root = element_tree.parse.return_value
        existing_walk_button = MagicMock()
        root.findall.return_value = [existing_walk_button]
        root.find.return_value = mappings_element
        key_transformer.transform.return_value = 'transformedkey'
        button_factory = ButtonFactory(
            config=config, key_transformer=key_transformer)

        button_factory.add(mappings_xpath, 'mapping_keymap')

        root.find.assert_called_once_with(mappings_xpath)
        existing_btn_el_xpath = '{0}//button[@modID="{1}"]'.format(
            mappings_xpath, config.get_walk_id())
        root.findall.assert_called_once_with(existing_btn_el_xpath)
        mappings_element.remove.assert_called_once_with(existing_walk_button)
