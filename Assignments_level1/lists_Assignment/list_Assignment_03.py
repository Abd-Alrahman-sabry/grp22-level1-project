lst = [1, 6, 3, 5, 3, 4]
num = 3
count_num = 0
new_list = []

for i in range(len(lst)):
    if lst[i] == num:
        print(num, ' is found on index =  ', i)
        new_list.append(lst[i])
        count_num = count_num + 1
    # elif lst[i] != num:                             # loop
        # print('number is not found')

if num not in lst:
    print('number is not found')


if num in lst:
    print('number is exist ', count_num, ' time/s')
    print(new_list)


