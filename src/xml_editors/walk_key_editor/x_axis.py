from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

from src.xml_editors.IDLocators import IDLocators


class XAxis:
    x_axis_xpath = './/mapping[@name="LeftX_Axis"]'

    def __init__(self, id_locators: IDLocators):
        super().__init__()
        self.id_locators = id_locators

    def put_forward(self, root: ElementTree):
        x_axis = root.find(self.x_axis_xpath)
        forward = x_axis.find('.//button[@overridableUI="forward"]')

        if forward is None:
            id = self.id_locators.forward(root)
            attributes = {'id': id, 'val': '0', 'overridableUI': 'forward'}
            SubElement(x_axis, 'button', attributes)
        else:
            forward.set('val', '0')

    def put_back(self, root):
        x_axis = root.find(self.x_axis_xpath)
        back = x_axis.find('.//button[@overridableUI="back"]')

        if back is None:
            id = self.id_locators.back(root)
            attributes = {'id': id, 'val': '0', 'overridableUI': 'back'}
            SubElement(x_axis, 'button', attributes)
        else:
            back.set('val', '0')
