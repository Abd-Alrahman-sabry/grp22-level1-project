def reverse_string(statement):
    statement_list = statement.split()
    statement_list.reverse()
    return ' '.join(statement_list)




str = "i like this program very much"
print(reverse_string(str))

