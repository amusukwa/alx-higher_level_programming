#!/usr/bin/python3
def text_indentation(text):
    """
    Prints text with indentation.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line = True
    for char in text:
        if new_line:
            if char == ' ':
                continue
            new_line = False
        print(char, end='')

        if char in '.:?':
            print('\n')
            new_line = True

