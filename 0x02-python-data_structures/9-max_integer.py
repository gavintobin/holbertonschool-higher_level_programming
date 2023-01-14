#!/usr/bin/python3
def max_integer(my_list=[]):
    bignum = my_list[0]
    for num in my_list:
        if num > bignum:
            bignum = num
    return bignum
