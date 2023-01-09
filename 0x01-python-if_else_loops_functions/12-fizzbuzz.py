#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0:
            print('Fizz'.format(), end=' ')
        elif i % 5 == 0:
            print('Buzz'.format(), end=' ')
        elif i % 15 == 0:
            print('FizzBuzz'.format(), end=' ')
        else:
            print('{}'.format(i), end=" ")
