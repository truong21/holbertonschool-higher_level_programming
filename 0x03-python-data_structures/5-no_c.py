#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for char in my_string:
        if ord(char) != ord('c') and ord(char) != ord('C'):
            str += char
    return str
