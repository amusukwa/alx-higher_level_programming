#!/usr/bin/python3
"""Reads a file"""


def read_file(filename=""):
    """This function reads text from a file"""
    try:
        file = open(filename, mode='r', encoding='utf-8')
        print(file.read(), end="")
        file.close()
    except FileNotFoundError:
        pass

