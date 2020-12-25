from xml.etree.ElementTree import ElementTree, SubElement

from src.xml_editors.IDLocators import IDLocators


class XAxis:
    x_axis_xpath = './/mapping[@name="LeftX_Axis"]'

    def __init__(self, id_locators: IDLocators):
        self.id_locators = id_locators

    def update_left(self, root):
        x_axis = root.find(self.x_axis_xpath)
        left = x_axis.find('.//button[@overridableUI="left"]')
        left.set('val', '-1.4')

    def update_right(self, root):
        x_axis = root.find(self.x_axis_xpath)
        right = x_axis.find('.//button[@overridableUI="right"]')
        right.set('val', '1.4')

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
