
with open('C:\\MY_FILES\\read_text.txt', 'r') as my_file_reference:
    content = my_file_reference.read()

with open('C:\\MY_FILES\\write_data2.txt', 'w') as my_file_reference:
    my_file_reference.write(content)
