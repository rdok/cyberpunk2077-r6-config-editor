class WalkKey:
    def put(self, root, walk_key):
        pass

    # def find(self):
    #     filename = self.config.get_input_user_mappings_path()
    #     root = ElementTree.parse(filename)
    #     mod_id = self.config.walk_id()
    #     return root.find(f'.//mapping[@modID="{mod_id}"]')
    # def put_walk_key(self, key, x_mapping: ElementTree, y_mapping: ElementTree):
    #     id = 'IK_{0}'.format(self.key_transformer.transform(key))
    #     mod_id = self.config.walk_id()
    #     attributes = {'id': id, 'val': '0', 'modID': mod_id}
    #
    #     x_element = x_mapping.find(f'.//button[@modID="{mod_id}"]')
    #     if x_element is None:
    #         x_element = SubElement(x_mapping, 'button', attributes)
    #         x_element.tail = '\n'
    #     else:
    #         x_element.set('id', id)
    #         x_element.set('val', '0')
    #
    #     y_element = y_mapping.find(f'.//button[@modID="{mod_id}"]')
    #     if y_element is None:
    #         y_element = SubElement(y_mapping, 'button', attributes)
    #         y_element.tail = '\n'
    #     else:
    #         y_element.set('id', id)
    #         y_element.set('val', '0')
    #
