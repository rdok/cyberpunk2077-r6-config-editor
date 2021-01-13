from abc import ABC

from src.frames.ToggleFrame import ToggleFrame


class DoubleTapDodgeFrame(ToggleFrame):
    def label_text(self):
        return 'DOUBLE TAP DODGE'

    def frame_row(self):
        return 4
