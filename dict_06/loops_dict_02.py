shopping_cart_dict = {'Milk': 40.0, 'Eggs': 160.0, 'Bread': 30.0}


print('---------1. loop over a dictionary KEYS using for each loop-------')
for key in shopping_cart_dict:
    print(key)
    print(shopping_cart_dict[key])
    print('---')




print('-----2. loop over a dictionary KEYS | Values using for each loopp-----')
for key, value in shopping_cart_dict.items():
    print(key)
    print(value)
    print('-----')
    