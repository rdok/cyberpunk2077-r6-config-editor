import os
import unittest

from src.config import Config

config = Config()


class TestConfig(unittest.TestCase):
    def test_it_configures_root_directory(self):
        path = os.path.join(os.path.dirname(__file__), '..', 'src')
        expected_root_dir = os.path.abspath(path)

        self.assertEqual(expected_root_dir, config.root_dir())

    def test_it_sets_the_input_user_mappings_path(self):
        self.assertEqual(None, config.get_input_user_mappings_path())
        config.set_input_user_mappings_path('r6/config/inputUserMappings.xml')
        path = os.path.abspath('r6/config/inputUserMappings.xml')
        self.assertEqual(path, config.get_input_user_mappings_path())

    def test_it_gets_the_walk_id(self):
        id = 'rdok/cyberpunk2077-r6-config-editor/walk'
        self.assertEqual(id, config.walk_id())

    def test_it_gets_the_app_name(self):
        self.assertEqual('Cyberpunk2077 r6-config-editor', config.app_name())

    def test_it_sets_the_input_contexts_path(self):
        self.assertEqual(None, config.get_input_contexts_path())
        config.set_input_contexts_path('r6/config/inputContexts.xml')
        path = os.path.abspath('r6/config/inputContexts.xml')
        self.assertEqual(path, config.get_input_contexts_path())
