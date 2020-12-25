from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

from src.xml_editors.IDLocators import IDLocators
from src.xml_editors.walk_key_editor.x_axis import XAxis


class XAxisBack(XAxis):
    def __init__(self, id_locators: IDLocators):
        super().__init__()
        self.id_locators = id_locators

    def put(self, root: ElementTree):
        x_axis = root.find(self.x_axis_xpath)
        back = x_axis.find('.//button[@overridableUI="back"]')

        if back is None:
            id = self.id_locators.back(root)
            attributes = {'id': id, 'val': '0', 'overridableUI': 'back'}
            SubElement(x_axis, 'button', attributes)
        else:
            back.set('val', '0')
