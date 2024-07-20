company_employees = [
(101, 'Ahmed Esam', 10000.0, 'Cairo'),
(102, 'Ibrahim Ahmed', 9000.0, 'Cairo'),
(103, 'Adham Aly', 5000.0, 'Cairo'),
(104, 'Islam Hassan', 7000.0, 'Cairo')
]
sum = 0
for i in range(len(company_employees)):
    sum = sum + company_employees[i][2]



print('Sum of salary of all employees = ', sum)
