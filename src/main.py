import os
import sys
from xml.etree import ElementTree

import getopt

DIR_NAME = os.path.dirname(__file__)


def capitilize_message(value):
    return value.upper()


def main(argv):
    INPUT_USER_MAPPINGS_REL_PATH = 'r6/config/inputUserMappings.xml'

    opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])

    filename = os.path.join(DIR_NAME, INPUT_USER_MAPPINGS_REL_PATH)
    tree = ElementTree.parse(filename)
    root = tree.getroot()

    print(root)


if __name__ == "__main__":
    main(sys.argv[1:])
