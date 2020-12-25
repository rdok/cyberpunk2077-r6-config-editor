# @patch('src.xml_editors.walk_element.ElementTree')
# def test_locates_itself(self, element_tree):
#     filename = self.config.get_input_user_mappings_path.return_value
#     root = element_tree.parse.return_value
#     expected_element = root.find.return_value
#     walk_id = self.config.walk_id.return_value
#
#     actual_element = self.element.find()
#
#     element_tree.parse.assert_called_once_with(filename)
#     root.find.assert_called_once_with(f'.//mapping[@modID="{walk_id}"]')
#     self.assertEqual(expected_element, actual_element)
#
