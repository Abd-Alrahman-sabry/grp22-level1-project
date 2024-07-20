def get_max_num(my_list):
    max_num = 0
    for num in my_list:
        if num > max_num:
            max_num = num
    return max_num


def get_min_num(my_list):
    min_num = my_list[0]
    for num in my_list:
        if num < min_num:
            min_num = num
    return min_num


new_list = [1, 2, 17, 4, 5]
print('Max Number in the list = ', get_max_num(new_list))
print('Min Number in the list = ', get_min_num(new_list))
