from abc import ABC

from src.xml_editors.ContextsEditor import ContextsEditor


class HoldActionEditor(ContextsEditor, ABC):
    def get_timeout(self):
        element = self.get()
        return element.get("timeout")

    def set_timeout(self, new_timeout):
        element = self.get()
        element.set("timeout", str(new_timeout))
        self.write()
