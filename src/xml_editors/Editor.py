from abc import ABC, abstractmethod
from xml.etree import ElementTree
from xml.etree.ElementTree import XMLParser

from src.Config import Config
from src.xml_editors.CustomTreeBuilder import CustomTreeBuilder


class Editor(ABC):
    def __init__(self, config: Config, parser: CustomTreeBuilder):
        self.parser = parser
        self.filename = config.get_input_contexts_path()

    def get(self):
        parser = XMLParser(target=CustomTreeBuilder())
        self.root = ElementTree.parse(self.filename, parser=parser)
        return self.root.find(self.get_xpath())

    @abstractmethod
    def get_xpath(self) -> str:
        pass
