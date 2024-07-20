str1 = 'ArabRepublicOfEgypt'
print('The original string is : ' + str1)
str1 = str1.lower()
no = int(len(str1) * 1/2)


str1_lst = str1.split()
for i in range(len(str1_lst)):
    str1_lst[i] = str1_lst[i][:no] + str1_lst[i][no:].upper()


str1 = ' '.join(str1_lst)
print('The resultant string : ' + str1)