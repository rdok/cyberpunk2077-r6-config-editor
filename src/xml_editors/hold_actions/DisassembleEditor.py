from src.xml_editors.hold_actions.HoldActionEditor import HoldActionEditor


class DisassembleEditor(HoldActionEditor):
    def get_xpath(self):
        return './/hold[@action="disassemble_item"]'
