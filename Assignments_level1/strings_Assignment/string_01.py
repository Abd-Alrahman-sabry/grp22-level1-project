str = "A comruter science portal for portal"
word = "portal"
count = 0
str_lst = str.split()
for item in str_lst:
    if item == word:
        count += 1

print(count)

