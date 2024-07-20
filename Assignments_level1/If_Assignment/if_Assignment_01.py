grade = int(input('please enter your grade: '))
A = 'Excellent'
B = 'V. Good'
C = 'Good'
D = 'Pass'
E = 'Fail'
if 90 <= grade <= 100:
    print(A)
elif 80 <= grade <= 90:
    print(B)
elif 70 <= grade <= 80:
    print(C)
elif 50 <= grade <= 70:
    print(D)
elif 0 <= grade <= 50:
    print(E)
else:
    print('invalid input')


