from src.Config import Config
from src.xml_editors.CustomTreeBuilder import CustomTreeBuilder
from src.xml_editors.Editor import Editor


class MappingsEditor(Editor):
    def __init__(self, config: Config, parser: CustomTreeBuilder):
        super().__init__(config, parser)
        self.__filename = config.get_input_user_mappings_path()

    def get_filename_path(self):
        return self.__filename
