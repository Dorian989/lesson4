from sys import argv

script_name, hour, stavka, prem = argv

print("Script name: ", script_name)
print("Work in hour: ", int(hour))
print("Rate: ", int(stavka))
print("Prize: ", int(prem))
print(f'raschet = {((int(hour) * int(stavka)) + int(prem))}')
