from src.config import Config
from xml.etree import ElementTree


class CraftingSpeedElement:
    def __init__(self, config: Config):
        self.config = config

    def modify(self, value):
        pass

    def get_timeout(self):
        filename = self.config.get_input_contexts_path()
        root = ElementTree.parse(filename)
        crafting_element = root.find('.//hold[@action="craft_item"]')

        return crafting_element.get('timeout')