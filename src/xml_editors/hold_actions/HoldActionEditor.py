from abc import ABC

from src.xml_editors.Editor import Editor


class HoldActionEditor(Editor, ABC):

    def get_timeout(self):
        element = self.get()
        return element.get('timeout')

    def set_timeout(self, new_timeout):
        element = self.get()
        element.set('timeout', str(new_timeout))
        self.root.write(self.filename, xml_declaration=True, encoding='utf8')
