from math import factorial
from time import sleep


def while_fatorial(n):
    f = 1
    print(f'{n}! = ', end='')
    sleep(0.5)
    while n > 0:
        print(f'{n}', end='')
        print(' x ' if n > 1 else ' = ', end='')
        f *= n
        n -= 1
    return f'{f}'


def for_fatorial(n):
    f = 1
    print(f'{n}! = ', end='')
    sleep(0.5)
    for i in range(n, 0, -1):
        print(f'{i}', end='')
        print(' x ' if i > 1 else ' = ', end='')
        f *= i
    return f' = {f}'