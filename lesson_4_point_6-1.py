from itertools import cycle

svet = 0
my_list = ['Green', 'yellow', 'Red']
for elem in cycle(my_list):
    if svet > 10:
        break
    print(elem)
    svet += 1