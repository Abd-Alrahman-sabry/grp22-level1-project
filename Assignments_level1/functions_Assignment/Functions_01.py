def rec_area(length, width):
    return length * width


length_rec = int(input('Enter the length of the rectangle : '))
width_rec = int(input('Enter the width of the rectangle : '))
area = rec_area(length_rec, width_rec)
print('The area of the rectangle is', area)

