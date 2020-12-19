from xml.etree.ElementTree import SubElement


class SlowWalkElement:
    def append_to(self, mappings_xpath, element_tree):
        walk_overridable_ui = 'slowWalk'
        slow_walk_button_element_xpath = '{0}{1}{2}{3}'.format(
            mappings_xpath,
            '//button[@id="IK_CapsLock"][@val="0"][@overridableUI="',
            walk_overridable_ui,
            '"]'
        )
        slow_walk_button_element = element_tree.find(
            slow_walk_button_element_xpath
        )

        if slow_walk_button_element is not None:
            return False

        attributes = {
            'id': 'IK_CapsLock',
            'val': '0',
            'overridableUI': walk_overridable_ui
        }
        mappings_element = element_tree.find(mappings_xpath)
        element = SubElement(mappings_element, 'button', attributes)
        element.tail = '\n'

        return True
