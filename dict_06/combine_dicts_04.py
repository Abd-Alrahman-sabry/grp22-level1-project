# program to combine dict1, dict2 into dict 1 with the same key adding values
dict1 = {'a': 100, 'b': 150, 'c': 100}
dict2 = {'a': 50, 'c': 100, 'd': 150}


# 1. loop over dict2
for key, value in dict2.items():
    if key in dict1:
        dict1[key] = dict1[key] + value
    else:
        dict1[key] = dict2[key]


print(dict1)