#!/usr/bin/python3
for i in range(1, 100):
    if i < 99:
        print('{:02d}'.format(i), end=', ')
print('{:02d}'.format(i), end='\n')
