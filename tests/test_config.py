# import os
import os
import unittest

from src.config import Config


class TestConfig(unittest.TestCase):
    def test_it_configures_root_directory(self):
        config = Config()
        path = os.path.join(os.path.dirname(__file__), '..', 'src')
        expected_root_dir = os.path.abspath(path)

        self.assertEqual(expected_root_dir, config.root_dir())

    def test_it_sets_the_input_user_mappings_path(self):
        config = Config()

        self.assertEqual(None, config.get_input_user_mappings_path())

        config.set_input_user_mappings_path('mocked_path')

        self.assertEqual('mocked_path', config.get_input_user_mappings_path())
