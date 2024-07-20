import csv

people_list = [
        ['Name', 'Age', 'City'],
        ['Adham', 25, 'Assuit'],
        ['Esam', 30, 'Cairo'],
        ['Shady', 28, 'Mansoura'],
        ['Omar', 30, 'Cairo'],
        ['Omnia', 22, 'Cairo'],
        ['Ahmed', 15, 'Alex']

]

with open("C:\\MY_FILES\\people.csv", 'w', newline='') as my_file_reference:
    write_pen = csv.writer(my_file_reference)
    for item in people_list:
        write_pen.writerow(item)

    """ 
    write_pen.writerow(['id', 'name', 'Salary'])
    write_pen.writerow(['101', 'Yahya', '7000'])
    write_pen.writerow(['102', 'Omar', '5000'])
    write_pen.writerow(['103', 'Hoda', '9000'])
    """
