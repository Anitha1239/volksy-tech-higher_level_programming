#!/usr/bin/python3
"""write a file"""


def append_write(filename="", text=""):
    """append"""
    if filename:
        with open(filename, mode='a', encoding="utf-8") as f:
            return(f.write(text))
