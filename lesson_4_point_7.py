from math import factorial
from itertools import count


def generator():
    for el in count(1):
        yield factorial(el)

gen = generator()
n = int(input('Enter digit: '))
x= 0
for i in gen:
    if x < n:
        print(i)
        x += 1
    else:
        break