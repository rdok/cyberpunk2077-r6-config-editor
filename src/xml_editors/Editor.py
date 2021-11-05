from abc import ABC, abstractmethod
from xml.etree import ElementTree
from xml.etree.ElementTree import XMLParser, Element

from src.xml_editors.CustomTreeBuilder import CustomTreeBuilder


class Editor(ABC):
    __root: ElementTree
    __filename: str

    def __init__(self, filename: str):
        self.__filename = filename
        self.parse_xml_file()

    def parse_xml_file(self):
        parser = XMLParser(target=CustomTreeBuilder())
        filename = self.__filename
        self.__root = ElementTree.parse(source=filename, parser=parser)

    def find(self, xpath) -> Element:
        self.parse_xml_file()
        return self.__root.find(xpath)

    def write(self):
        self.__root.write(self.__filename, xml_declaration=True, encoding="utf8")

    def get(self):
        self.parse_xml_file()
        return self.find(xpath=self.get_xpath())

    @abstractmethod
    def get_xpath(self):
        pass
