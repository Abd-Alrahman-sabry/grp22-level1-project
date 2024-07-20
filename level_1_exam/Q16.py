company_employees = [

    (101, 'Hayam Esam', 10000.0, 'Engineer', 'F'),

    (102, 'Ibrahim Ahmed', 9000.0, 'Accountant', 'M'),

    (103, 'Adham Aly', 5000.0, 'Engineer', 'M'),

    (104, 'Islam Hassan', 7000.0, 'Sales', 'M'),

    (105, 'Marwa Esam', 7000.0, 'Marketer', 'F'),

    (106, 'Ola Hassan', 7000.0, 'Engineer', 'F')

    ]

count_male, count_female = 0, 0

for i in range(len(company_employees)):
    if company_employees[i][4] == 'F':
        count_female += 1
    elif company_employees[i][4] == 'M':
        count_male += 1

print('number of male employees: ', count_male)
print('number of female employees: ', count_female)
