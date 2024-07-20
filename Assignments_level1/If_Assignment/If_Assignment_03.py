


oper = (input('===========Please choose a number for the operator============''\n 1 = +' '\n 2 = -''\n 3 = *''\n 4 = /   :'))
num1 = input('please enter the first number:')
num2 = input('please enter the second number:')



if oper == '1':
    result = int(num1) + int(num2)
    print(result)
elif oper == '2':
    result = int(num1) - int(num2)
    print(result)
elif oper == '3':
    result = int(num1) * int(num2)
    print(result)
elif oper == '4':
    result = int(num1) / int(num2)
    print(result)
else:
    print('Please choose a valid operator')