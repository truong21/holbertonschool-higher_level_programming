#!/usr/bin/python3
"""

Module containing text_indentation

"""


def text_indentation(text):
    """ prints a text with 2 new lines after each of these characters """
    if not isinstance(text, str) or text is None or len(text) < 0:
        raise TypeError("text must be a string")
    flag = 0
    for char in text:
        if char in ".:?":
            print(char)
            print("")
            flag = 1
        else:
            if flag == 0:
                print(char, end="")
            else:
                if char in " \t":
                    pass
                else:
                    print(char, end="")
                    flag = 0
