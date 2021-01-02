from src.frames.hold_actions.HoldActionFrame import HoldActionFrame
from src.xml_editors.hold_actions.HoldActionEditor import HoldActionEditor


class CraftingFrame(HoldActionFrame):
    def __init__(self, editor: HoldActionEditor):
        super().__init__(editor)

    def label_text(self) -> str:
        return 'CRAFTING SPEED'

    def from_(self) -> float:
        return 0.01

    def to_(self) -> float:
        return 1.0

    def resolution(self) -> float:
        return 0.01

    def frame_row(self) -> int:
        return 2
