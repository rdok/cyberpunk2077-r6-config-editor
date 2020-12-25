from xml.etree import ElementTree


class IDLocators:
    def back(self, root: ElementTree):
        xpath = './/mapping[@name="LeftY_Axis"]' \
                '//button[@overridableUI="back"]'
        element = root.find(xpath)
        return element.get('id')

    def forward(self, root):
        xpath = './/mapping[@name="LeftY_Axis"]' \
                '//button[@overridableUI="forward"]'
        element = root.find(xpath)
        return element.get('id')

    def left(self, root):
        xpath = './/mapping[@name="LeftX_Axis"]' \
                '//button[@overridableUI="left"]'
        element = root.find(xpath)
        return element.get('id')

    def right(self, root):
        xpath = './/mapping[@name="LeftX_Axis"]' \
                '//button[@overridableUI="right"]'
        element = root.find(xpath)
        return element.get('id')
