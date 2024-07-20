# create 4 functions
"""
1. add_numbers : which add 2 parameters and return result
2. multiply_numbers : which multiply 3 parameters and return result
3. divide_numbers : which divide 2 parameters and return result and check not to divide by Zero
4. abs_numbers : which take 1 parameter : if it is negative just return +ive of this number
"""

def add_numbers(first_number, second_number):
    return first_number + second_number


def multiply_numbers(first_number, second_number, third_number):
    return first_number * second_number * third_number


def divide_numbers(first_number, second_number):
    if second_number == 0:
        return 'Error - Cannot Divide by Zero'
    else:
        return first_number / second_number

def abs_numbers(value):
    if value < 0:
        return value * (-1)
    else:
        return value


# main program
# calling to all functions

add_result = add_numbers(7, 8)
multiply_result = multiply_numbers(9, 6, 3)
abs_result = abs_numbers(-20)
divide_result = divide_numbers(8, 5)
print(add_result, multiply_result, divide_result, abs_result)
