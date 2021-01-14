from src.xml_editors.ContextsEditor import ContextsEditor


class DoubleTapDodgeEditor(ContextsEditor):
    def get_xpath(self):
        return {
            'forward': './/multitap[@action="DodgeForward"]',
            'right': './/multitap[@action="DodgeRight"]',
            'back': './/multitap[@action="DodgeBack"]',
            'left': './/multitap[@action="DodgeLeft"]',
        }

    def is_enabled(self) -> bool:
        xpath = self.get_xpath().get('forward')
        element = self.find(xpath)
        return element.get('count') == '2'

    def disable(self):
        xpath = self.get_xpath().get('forward')
        element = self.find(xpath)
        element.set('count', 99)
