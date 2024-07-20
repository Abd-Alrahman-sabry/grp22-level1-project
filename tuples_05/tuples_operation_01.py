
print('---- create and print tuple -----')
my_tuple = (101, 'Mostafa', 8000.0, 'Giza')
print(my_tuple)
print(type(my_tuple))




print('---------- access element in a tuple by index -------------')

print(my_tuple[3])



print('------------ un packing tuple ----- ')
emp_code, emp_name, emp_salary, emp_adress = my_tuple
print(emp_code, emp_name, emp_salary, emp_adress)


print('------ Loop over Tuple -------')

for items in my_tuple:
    print(items)


