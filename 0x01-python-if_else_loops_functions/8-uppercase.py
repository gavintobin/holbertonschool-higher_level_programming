#!/usr/bin/python3
def uppercase(str):
    ns = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 123:
            ns = ns + chr(ord(char) - 32)
        else:
            ns = ns + char
    print('{}'.format(ns))
