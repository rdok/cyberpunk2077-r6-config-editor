from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement, XMLParser

from src.Config import Config
from src.transformers.KeyTransformer import KeyTransformer
from src.xml_editors.CustomTreeBuilder import CustomTreeBuilder
from src.xml_editors.walk_key_editor.axis import Axis


class WalkKey(Axis):
    def __init__(
        self,
        config: Config,
        transformer: KeyTransformer,
        parser: CustomTreeBuilder
    ):
        self.parser = parser
        self.transformer = transformer
        self.config = config

    def find(self):
        filename = self.config.get_input_user_mappings_path()
        parser = XMLParser(target=self.parser)
        root = ElementTree.parse(filename, parser=parser)
        mod_id = self.config.walk_id()

        path = '{0}//button[@modID="{1}"]'.format(self.x_axis_xpath, mod_id)
        return root.find(path)

    def put(self, key, root: ElementTree):
        x_axis = root.find(self.x_axis_xpath)
        y_axis = root.find(self.y_axis_xpath)
        id = 'IK_{0}'.format(self.transformer.transform(key))
        mod_id = self.config.walk_id()
        attributes = {'id': id, 'val': '0', 'modID': mod_id}
        x_axis_walk = x_axis.find(f'.//button[@modID="{mod_id}"]')
        y_axis_walk = y_axis.find(f'.//button[@modID="{mod_id}"]')

        if x_axis_walk is None:
            x_axis_walk = SubElement(x_axis, 'button', attributes)
            x_axis_walk.tail = '\n'
        else:
            x_axis_walk.set('id', id)
            x_axis_walk.set('val', '0')

        if y_axis_walk is None:
            y_axis_walk = SubElement(y_axis, 'button', attributes)
            y_axis_walk.tail = '\n'
        else:
            y_axis_walk.set('id', id)
            y_axis_walk.set('val', '0')
