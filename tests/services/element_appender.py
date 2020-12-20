import unittest


class ElementAppender(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


    #
    # @patch('src.slow_walk_element.SubElement')
    # def test_it_should_not_duplicate_slow_walk_button(self, sub_element):
    #     tree = MagicMock()
    #     existing_slow_walk_button_el = MagicMock()
    #     tree.find.side_effect = [existing_slow_walk_button_el]
    #
    #     slow_walk_element = ElementAppender()
    #     slow_walk_btn_el_created = slow_walk_element.append_to(
    #         'mapping_xpath', tree
    #     )
    #
    #     sub_element.assert_not_called()
    #     self.assertFalse(slow_walk_btn_el_created)


