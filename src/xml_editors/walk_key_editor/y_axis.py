from xml.etree.ElementTree import ElementTree, SubElement

from src.xml_editors.IDLocators import IDLocators


class YAxis:
    y_axis_xpath = './/mapping[@name="LeftY_Axis"]'

    def __init__(self, id_locators: IDLocators):
        self.id_locators = id_locators

    def put_left(self, root):
        y_axis = root.find(self.y_axis_xpath)
        left = y_axis.find('.//button[@overridableUI="left"]')

        if left is None:
            id = self.id_locators.left(root)
            attributes = {'id': id, 'val': '0', 'overridableUI': 'left'}
            sub_element = SubElement(y_axis, 'button', attributes)
            sub_element.tail = '\n'
        else:
            left.set('val', '0')

    def put_right(self, root):
        y_axis = root.find(self.y_axis_xpath)
        right = y_axis.find('.//button[@overridableUI="right"]')

        if right is None:
            id = self.id_locators.right(root)
            attributes = {'id': id, 'val': '0', 'overridableUI': 'right'}
            sub_element = SubElement(y_axis, 'button', attributes)
            sub_element.tail = '\n'
        else:
            right.set('val', '0')

    def update_forward(self, root: ElementTree):
        y_axis = root.find(self.y_axis_xpath)
        right = y_axis.find('.//button[@overridableUI="forward"]')
        right.set('val', '1.4')

    def update_back(self, root):
        y_axis = root.find(self.y_axis_xpath)
        back = y_axis.find('.//button[@overridableUI="back"]')
        back.set('val', '-1.4')
