from abc import ABC, abstractmethod

from src.xml_editors.ContextsEditor import ContextsEditor


class ToggleEditor(ContextsEditor, ABC):

    @abstractmethod
    def is_enabled(self) -> bool:
        pass
