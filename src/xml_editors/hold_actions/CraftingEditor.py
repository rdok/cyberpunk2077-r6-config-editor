from src.xml_editors.hold_actions.HoldActionEditor import HoldActionEditor


class CraftingEditor(HoldActionEditor):
    def get_xpath(self):
        return './/hold[@action="craft_item"]'
