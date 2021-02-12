my_old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [elem for num, elem in enumerate(my_old_list) if my_old_list[num - 1] < my_old_list[num]]
print(my_old_list)
print(my_new_list)
