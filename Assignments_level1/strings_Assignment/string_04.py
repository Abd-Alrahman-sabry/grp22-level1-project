str1 = 'Hello world world Python is great great Python'
new_str_lst =[]
str1_lst = str1.split()
print("Original String: ", str1)


for i in range(len(str1_lst)):
    if str1_lst[i] not in new_str_lst:
        new_str_lst.append(str1_lst[i])



str1 = ' '.join(new_str_lst)

print("String after removing duplicates : ", str1)
