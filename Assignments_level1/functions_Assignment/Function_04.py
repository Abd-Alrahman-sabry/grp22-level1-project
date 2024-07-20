def sum_positive_numbers(lst):
    total = 0
    for item in lst:
        if item > 0:
            total = item + total
    return total


def count_positive_numbers(list_1):
    count = 0
    for item in list_1:
        if item > 0:
            count += 1
    return count


new_lst = [5, -7, -9, -11, 2, 3, 4]
sum_pos = sum_positive_numbers(new_lst)
print('Sum Of Positive Numbers In The List = ', sum_pos)

count_pos = count_positive_numbers(new_lst)
print('and its count = ', count_pos)
