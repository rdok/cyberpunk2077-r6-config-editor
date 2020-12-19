import os
from argparse import ArgumentParser
from xml.etree import ElementTree

from src.slow_walk_element import SlowWalkElement

DIR_NAME = os.path.dirname(__file__)


def capitilize_message(value):
    return value.upper()


def main(args, ioc):
    filename = os.path.join(DIR_NAME, args.input_user_mappings_path)
    tree = ElementTree.parse(filename)

    slow_walk_element = ioc.get(SlowWalkElement.__name__)

    y_axis_xpath = './/mapping[@name="LeftY_Axis"][@type="Axis"]'
    slow_walk_element.append_to(y_axis_xpath, tree)

    x_axis_xpath = './/mapping[@name="LeftX_Axis"][@type="Axis"]'
    slow_walk_element.append_to(x_axis_xpath, tree)

    tree.write(filename)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-i",
        "--input_user_mappings_path",
        dest="input_user_mappings_path",
        default='r6/config/inputUserMappings.xml'
    )
    args = parser.parse_args()

    dependencies = {SlowWalkElement.__name__: SlowWalkElement()}

    main(args, dependencies)
