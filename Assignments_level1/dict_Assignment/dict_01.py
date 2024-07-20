colors_list = [('red', 223), ('blue', 201), ('green', 210)]
colors_dict = {}


for i in range (len(colors_list)):                                # solution 1
    colors_dict[colors_list[i][0]] = colors_list[i][1]


print(colors_dict)


# colors_dict = dict(colors_list)                                 # solution 2
# print(colors_dict)