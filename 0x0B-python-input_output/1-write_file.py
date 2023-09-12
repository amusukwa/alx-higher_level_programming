#!/usr/bin/python3
"""Writes to a file"""


def write_file(filename="", text=""):
    """This function wtites a string to a file"""
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
