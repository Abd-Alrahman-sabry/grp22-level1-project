# program to show dictionary operations
print('---- create and print dictionary -----')
shopping_cart_dict = {'Milk': 40.0, 'Eggs': 160.0, 'Bread': 30.0}
print(shopping_cart_dict)
print(type(shopping_cart_dict))
print(len(shopping_cart_dict))



print('------ Adding, change new pair to the dictionary -------')
shopping_cart_dict['Nescafe'] = 60.0
shopping_cart_dict['Milk'] = 45.0
print(shopping_cart_dict)



print('------ access element -----')
print('price of Eggs = ', shopping_cart_dict['Eggs'])
# add 25% to the price of Eggs
shopping_cart_dict['Eggs'] = shopping_cart_dict['Eggs'] + 25/100 * shopping_cart_dict['Eggs']
print(shopping_cart_dict)




print('---- delete element pair from dict ------')
shopping_cart_dict.pop('Bread')
print(shopping_cart_dict)



print('------ Concat Multi dictionaries ------')
home_cart_dict = {'Meat': 400.0, 'Chicken': 125.0, 'Milk': 60.0}
shopping_cart_dict.update(home_cart_dict)
print(shopping_cart_dict)