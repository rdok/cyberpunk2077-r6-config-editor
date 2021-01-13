from abc import ABC, abstractmethod

from src.xml_editors.Editor import Editor


class ToggleEditor(Editor, ABC):

    @abstractmethod
    def is_enabled(self) -> bool:
        pass
