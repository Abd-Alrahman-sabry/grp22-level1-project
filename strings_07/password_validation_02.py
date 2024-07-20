# program to validate complex password
password = 'egYpt_2024' # valid
count_upper, count_lower, count_digits, count_signs = 0, 0, 0, 0

if len(password) >= 8:
    for letter in password:
        if letter.isupper():
            count_upper += 1
        elif letter.islower():
            count_lower += 1
        elif letter.isdigit():
            count_digits += 1
        elif not letter.isalnum():
            count_signs += 1

    if count_upper and count_lower and count_digits and count_signs >= 1 :
        print('Valid Password')
    else:
        print('Invalid complex Password')

else:
    print('Invalid password - should > 8 letters')