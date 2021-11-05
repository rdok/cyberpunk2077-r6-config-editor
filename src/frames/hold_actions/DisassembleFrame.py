from src.frames.hold_actions.HoldActionFrame import HoldActionFrame
from src.xml_editors.hold_actions.DisassembleEditor import DisassembleEditor


class DisassembleFrame(HoldActionFrame):
    def __init__(self, editor: DisassembleEditor):
        super().__init__(editor)

    def label_text(self) -> str:
        return "DISASSEMBLE SPEED"

    def from_(self) -> float:
        return 0.01

    def to_(self) -> float:
        return 1.0

    def resolution(self) -> float:
        return 0.01

    def frame_row(self) -> int:
        return 3
