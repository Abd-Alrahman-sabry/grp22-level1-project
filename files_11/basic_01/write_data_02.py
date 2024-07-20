# program to write data to a text files

print('-----first way-----')

my_file_reference = open("C:\\MY_FILES\\write_data.txt", 'w')
my_file_reference.write("I like programming\n")
my_file_reference.write("I like football\n")
my_file_reference.write("Python is my favorite programming language\n")
my_file_reference.close()


print('-----second way-----using with----')
with open('C:\\MY_FILES\\write_data.txt') as my_file_reference:
    my_file_reference.write("\n")
    my_file_reference.write("My City is Cairo\n")
    my_file_reference.write("My City is Alex\n")
    my_file_reference.write("Iam an Engineer\n")
