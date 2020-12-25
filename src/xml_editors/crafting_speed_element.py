from xml.etree import ElementTree
from xml.etree.ElementTree import XMLParser

from src.config import Config
from src.xml_editors.CustomParser import CustomParser


class CraftingSpeedEditor:
    def __init__(self, config: Config, parser: CustomParser):
        self.parser = parser
        self.filename = config.get_input_contexts_path()

    def get_timeout(self):
        element = self.get()
        return element.get('timeout')

    def get(self):
        parser = XMLParser(target=CustomParser())
        self.root = ElementTree.parse(self.filename, parser=parser)
        return self.root.find('.//hold[@action="craft_item"]')

    def set_timeout(self, new_timeout):
        element = self.get()
        element.set('timeout', str(new_timeout))
        self.root.write(self.filename, xml_declaration=True, encoding='utf8')
