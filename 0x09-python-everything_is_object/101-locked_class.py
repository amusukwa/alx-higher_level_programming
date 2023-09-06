#!/usr/bin/python3
"""Defines a class"""

class LockedClass:
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '" + name + "'")
        else:
            super().__setattr__(name, value)
