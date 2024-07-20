str1 = str(input('Enter a string: '))

for letter in str1:
    if str1 == str1[::-1]:
        print("'", str1, "'", 'is a palindrome')
        break
    else:
        print("'", str1, "'", 'is not a palindrome')
        break

