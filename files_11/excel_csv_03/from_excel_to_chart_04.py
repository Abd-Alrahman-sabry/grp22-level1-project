import csv
import matplotlib.pyplot as plt

with open("C:\\MY_FILES\\people.csv", 'r') as my_file_reference:
    reader_pen = csv.reader(my_file_reference)
    reader_pen.__next__()
    x_axis = []
    y_axis = []
    for row in reader_pen:
        x_axis.append(row[0])
        y_axis.append(float(row[1]))

    plt.bar(x_axis, y_axis)
    plt.xlabel("Names")
    plt.ylabel("Ages")
    plt.title("Bar Chart from CSv Data")
    plt.xticks(rotation=45)
    plt.show()
