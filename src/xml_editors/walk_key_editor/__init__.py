from xml.etree import ElementTree
from xml.etree.ElementTree import XMLParser

from src.config import Config
from src.xml_editors.CustomParser import CustomParser
from src.xml_editors.walk_key_editor.walk_key import WalkKey
from src.xml_editors.walk_key_editor.x_axis import XAxis
from src.xml_editors.walk_key_editor.y_axis import YAxis


class WalkKeyEditor:
    def __init__(
        self,
        config: Config,
        x_axis: XAxis,
        y_axis: YAxis,
        walk_key: WalkKey,
        parser: CustomParser
    ):
        self.parser = parser
        self.y_axis = y_axis
        self.config = config
        self.x_axis = x_axis
        self.walk_key = walk_key

    def write(self, key: str):
        filename = self.config.get_input_user_mappings_path()

        parser = XMLParser(target=CustomParser())
        root = ElementTree.parse(filename, parser=parser)

        self.walk_key.put(key=key, root=root)
        self.x_axis.put_forward(root)
        self.x_axis.put_back(root)
        self.x_axis.update_left(root)
        self.x_axis.update_right(root)

        self.y_axis.put_left(root)
        self.y_axis.put_right(root)
        self.y_axis.update_back(root)
        self.y_axis.update_forward(root)

        root.write(filename)
