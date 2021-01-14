from src.widgets.toggle_frame.ToggleFrame import ToggleFrame


class DoubleTapDodgeFrame(ToggleFrame):

    def label_text(self):
        return 'DOUBLE TAP DODGE'

    def frame_row(self):
        return 4

    def dispatch_disable_event(self):
        self.toggle_editor.disable()

    def dispatch_enable_event(self):
        self.toggle_editor.enable()
