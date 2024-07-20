#program to count , sum postive and negative numbrs in a list


my_list = [14, -7, 9, -2, 3, 10]

#for each loop

total_pos, total_neg, count_pos, count_neg, count_zeros = 0, 0, 0, 0, 0


for item in my_list:
    if item > 0:
        total_pos = total_pos + item
        count_pos = count_pos + 1
    elif item < 0:
        total_neg = total_neg + item
        count_neg = count_neg + 1
    else:
        count_zeros = count_zeros + 1


print('total_pos = ', total_pos, ' count_pos = ', count_pos)
print('total_neg = ', total_neg, ' count_neg = ', count_neg)
print('count_zeros = ', count_zeros)