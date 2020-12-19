import unittest
from unittest.mock import patch, MagicMock, call

from src.slow_walk_element import SlowWalkElement


class TestSlowWalkSubElementTest(unittest.TestCase):
    @patch('src.slow_walk_element.SubElement')
    def test_it_appends_a_slow_walk_button_element(self, sub_element):
        tree = MagicMock()
        existing_slow_walk_button_el = None
        mapping_element = MagicMock()
        tree.find.side_effect = [existing_slow_walk_button_el, mapping_element]

        slow_walk_element = SlowWalkElement()
        slow_walk_element_created = slow_walk_element.append_to(
            'mapping_xpath', tree
        )

        slow_walk_xpath = '{0}{1}'.format(
            'mapping_xpath',
            '//button[@id="IK_CapsLock"][@val="0"][@overridableUI="slowWalk"]'
        )

        tree.find.assert_has_calls([
            call(slow_walk_xpath),
            call('mapping_xpath')
        ])

        sub_element.assert_called_once_with(
            mapping_element,
            'button',
            {'id': 'IK_CapsLock', 'val': '0', 'overridableUI': 'slowWalk'}
        )

        self.assertEqual(sub_element.return_value.tail, '\n')
        self.assertTrue(slow_walk_element_created)

    @patch('src.slow_walk_element.SubElement')
    def test_it_should_not_duplicate_slow_walk_button(self, sub_element):
        tree = MagicMock()
        existing_slow_walk_button_el = MagicMock()
        tree.find.side_effect = [existing_slow_walk_button_el]

        slow_walk_element = SlowWalkElement()
        slow_walk_btn_el_created = slow_walk_element.append_to(
            'mapping_xpath', tree
        )

        sub_element.assert_not_called()
        self.assertFalse(slow_walk_btn_el_created)
