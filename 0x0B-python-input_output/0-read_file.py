#!/usr/bin/python3
"""Reads a file"""


def read_file(filename=""):
    """This function reads a text file"""
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            print(file.read(), end="")
    except FileNotFoundError:
        pass
