shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}
sum_value = 0
for key in shopping_cart_dict:
    shopping_cart_dict[key] = shopping_cart_dict[key] + 10/100 * shopping_cart_dict[key]
    sum_value += shopping_cart_dict[key]


print('shopping cart after 10% raise = ', shopping_cart_dict)
print('Total = ', sum_value)
total_net = sum_value + 14/100 * sum_value
print('Total net = ', total_net)
