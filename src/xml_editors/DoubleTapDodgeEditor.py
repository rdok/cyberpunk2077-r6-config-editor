from src.widgets.toggle_frame.ToggleEditor import ToggleEditor
from src.xml_editors.ContextsEditor import ContextsEditor


class DoubleTapDodgeEditor(ContextsEditor, ToggleEditor):
    xpaths = {
        'forward': './/multitap[@action="DodgeForward"]',
        'right': './/multitap[@action="DodgeRight"]',
        'back': './/multitap[@action="DodgeBack"]',
        'left': './/multitap[@action="DodgeLeft"]',
    }

    def get_xpath(self):
        return self.xpaths

    def is_enabled(self) -> bool:
        xpath = self.get_xpath().get('forward')
        element = self.find(xpath)
        return element.get('count') == '2'

    def disable(self):
        for xpath in self.get_xpath().values():
            self.disable_dodge(xpath)
        self.write()

    def disable_dodge(self, xpath):
        self.set_count('99', xpath)

    def enable_dodge(self, xpath):
        self.set_count('2', xpath)

    def set_count(self, count, xpath):
        element = self.find(xpath)
        element.set('count', count)

    def enable(self):
        for xpath in self.get_xpath().values():
            self.enable_dodge(xpath)
        self.write()
