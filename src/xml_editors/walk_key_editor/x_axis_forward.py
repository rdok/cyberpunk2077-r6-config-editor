from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

from src.xml_editors.IDLocators import IDLocators
from src.xml_editors.walk_key_editor.x_axis import XAxis


class XAxisForward(XAxis):
    def __init__(self, id_locators: IDLocators):
        super().__init__()
        self.id_locators = id_locators

    def put(self, root: ElementTree):
        x_axis = root.find(self.x_axis_xpath)
        forward = x_axis.find('.//button[@overridableUI="forward"]')

        if forward is None:
            id = self.id_locators.forward(root)
            attributes = {'id': id, 'val': '0', 'overridableUI': 'forward'}
            SubElement(x_axis, 'button', attributes)
        else:
            forward.set('val', '0')
