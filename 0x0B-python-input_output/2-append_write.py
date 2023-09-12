#!/usr/bin/python3
""" Appends string to text"""


def append_write(filename="", text=""):
    """ This functions appends string to the end of a text file"""
    try:
        with open(filename, mode='a', encoding='utf-8') as file:
            return file.write(text)
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
