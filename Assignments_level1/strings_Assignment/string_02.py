str1 = "python exercises practis solution"
str1 = str1.title()
str1 = str1 [::-1]

str1_lst = str1.split()
print(str1_lst)

for i in range(len(str1_lst)):
    str1_lst[i] = str1_lst[i][0].upper() + str1_lst[i][1:]
    str1_lst[i] = str1_lst[i] [::-1]

print(str1_lst)
