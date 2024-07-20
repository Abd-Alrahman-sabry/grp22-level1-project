def element_exists(my_list, num):
    index_lst = []
    for i in range(len(my_list)):
        if my_list[i] == num:
            index_lst.append(i)

    return index_lst


lst = [1, 2, 3, 4, 5, 2]
index_shows = element_exists(lst, 2)
print('element shows in indexes : ', index_shows)
