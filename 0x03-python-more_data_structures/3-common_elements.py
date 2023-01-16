#!/usr/bin/python3
def common_elements(set_1, set_2):
    one = set(set_1)
    two = set(set_2)

    if (one & two):
        print(one & two)
