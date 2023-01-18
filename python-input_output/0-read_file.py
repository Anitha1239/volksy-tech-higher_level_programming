#!/usr/bin/python3
"""input-output
"""


def read_file(filename=""):
    """input-output-programs
    """

    with open(filename, encoding="utf-8") as readFile:
        print(readFile.read(), end='')
