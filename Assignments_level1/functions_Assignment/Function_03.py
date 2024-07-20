def prime_numbers(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return False
        elif n % i != 0:
            return True
    return False


check_num = int(input("Enter a number: "))
print(check_num, 'is a prime number?')

num = prime_numbers(check_num)
print(num)
