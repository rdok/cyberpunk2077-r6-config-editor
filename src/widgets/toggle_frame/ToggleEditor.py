from abc import ABC, abstractmethod


class ToggleEditor(ABC):

    @abstractmethod
    def is_enabled(self) -> bool:
        pass

    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def enable(self):
        pass
