str1 = str(input("Enter a string: "))

str1_lst = []

for i in str1:
    str1_lst.append(i)


str1_lst.sort()
str1 = ''.join(str1_lst)
print(str1)