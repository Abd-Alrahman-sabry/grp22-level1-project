shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}
print('shopping cart = ', shopping_cart_dict)
sum = 0

for key in shopping_cart_dict:
    shopping_cart_dict[key] = shopping_cart_dict[key] + 10/100 * shopping_cart_dict[key]
    sum += shopping_cart_dict[key]

print('shopping cart after 10% raise = ', shopping_cart_dict)
print('Total = ', sum)
total_net = sum + 14/100 * sum
print('Total net = ', total_net)



