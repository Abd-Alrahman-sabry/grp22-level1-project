def remove_special(statement):
    new_statement = ''
    for i in statement:
        if i.isalnum():
            new_statement = new_statement + i
    return new_statement


ini_string = "123abcjw:, .@! eiw"
new_string = remove_special(ini_string)
print(new_string)
