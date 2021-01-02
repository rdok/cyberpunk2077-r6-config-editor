from abc import ABC, abstractmethod
from xml.etree import ElementTree
from xml.etree.ElementTree import XMLParser

from src.Config import Config
from src.xml_editors.CustomTreeBuilder import CustomTreeBuilder


class HoldActionEditor(ABC):
    def __init__(self, config: Config, parser: CustomTreeBuilder):
        self.parser = parser
        self.filename = config.get_input_contexts_path()

    def get_timeout(self):
        element = self.get()
        return element.get('timeout')

    def get(self):
        parser = XMLParser(target=CustomTreeBuilder())
        self.root = ElementTree.parse(self.filename, parser=parser)
        return self.root.find(self.get_xpath())

    def set_timeout(self, new_timeout):
        element = self.get()
        element.set('timeout', str(new_timeout))
        self.root.write(self.filename, xml_declaration=True, encoding='utf8')

    @abstractmethod
    def get_xpath(self) -> str:
        pass
