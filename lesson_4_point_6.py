from itertools import count

for elem in count(int(input('Enter start digit '))):
    print(elem)
    if elem == 10:
        break