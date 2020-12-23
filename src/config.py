import os

import src


class Config:
    input_contexts_path = None
    input_user_mappings_path = None

    def root_dir(self):
        return os.path.dirname(src.__file__)

    def get_input_user_mappings_path(self):
        return self.input_user_mappings_path

    def set_input_user_mappings_path(self, value):
        path = os.path.abspath(value)
        self.input_user_mappings_path = path

    def walk_id(self):
        return 'rdok/cyberpunk2077-r6-config-editor/walk'

    def app_name(self):
        return 'Cyberpunk2077 r6-config-editor'

    def set_input_contexts_path(self, value):
        path = os.path.abspath(value)
        self.input_contexts_path = path

    def get_input_contexts_path(self):
        return self.input_contexts_path
