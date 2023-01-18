#!/usr/bin/python3
"""zero task in input/output
"""


def read_file(filename=""):
    """functions only
    """
    
with open(filename, encoding="utf-8") as readFile:
    print(readFile.read(),end='')
