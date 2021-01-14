from abc import ABC, abstractmethod
from xml.etree import ElementTree
from xml.etree.ElementTree import XMLParser, Element

from src.xml_editors.CustomTreeBuilder import CustomTreeBuilder


class Editor(ABC):
    def __init__(self, filename: str, parser: CustomTreeBuilder):
        self.parser = parser
        self.__filename = filename

        parser = XMLParser(target=CustomTreeBuilder())
        self.__root = ElementTree.parse(self.__filename, parser=parser)

    def find(self, xpath) -> Element:
        return self.__root.find(xpath)

    def write(self):
        self.__root.write(self.__filename, xml_declaration=True, encoding='utf8')

    def get(self):
        return self.find(xpath=self.get_xpath())

    @abstractmethod
    def get_xpath(self):
        pass
