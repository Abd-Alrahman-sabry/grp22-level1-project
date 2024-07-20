def pass_valid(pass_value):
    count_lower, count_upper, count_digit, count_special = 0, 0, 0, 0
    if len(pass_value) >= 8:
        for char in pass_value:
            if char.islower():
                count_lower += 1
            elif char.isupper():
                count_upper += 1
            elif char.isdigit():
                count_digit += 1
            elif not char.isalnum():
                count_special += 1
        if count_lower > 0 and count_upper > 0 and count_digit > 0 and count_special > 0:
            return True
    return False





str = "sr@m@_f0rtu9e$._2023"
print(pass_valid(str))







