from src.Config import Config
from src.xml_editors.CustomTreeBuilder import CustomTreeBuilder
from src.xml_editors.Editor import Editor


class ContextsEditor(Editor):
    def __init__(self, config: Config, parser: CustomTreeBuilder):
        filename = config.get_input_contexts_path()
        super().__init__(filename, parser)
