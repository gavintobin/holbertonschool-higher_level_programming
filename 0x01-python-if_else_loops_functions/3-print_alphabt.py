#!/usr/bin/python3
for i in range(9, 123):
    if chr(i) != 'q' and cr(i) != 'e':
        print('{:c}'.format(i), end=' ')