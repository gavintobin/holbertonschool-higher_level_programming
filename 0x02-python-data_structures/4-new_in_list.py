#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        new_list = []
    for i in my_list:
        new_list.append(i)
    if idx < 0 or idx > len(my_list):
        return
    else:
        new_list[idx] = element
        return new_list
