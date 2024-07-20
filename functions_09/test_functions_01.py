# function named print_numbers to print numbers from 1 to Max_Value

def print_numbers(max_value):
    total = 0
    for i in range(1, max_value + 1):
        print(i, end=" ")
        total += i
    print('')
    return total


# main Program
print('My Main Program')
# calling function
result_total_10 = print_numbers(10)
print('total of numbers between 1 to 10 : ', result_total_10, '\n')

result_total_20 = print_numbers(20)
print('total of numbers between 1 to 20 : ', result_total_20, '\n')
result_total_100 = print_numbers(100)
print('total of numbers between 1 to 100 : ', result_total_100, '\n')
print('Continue Main Program')
