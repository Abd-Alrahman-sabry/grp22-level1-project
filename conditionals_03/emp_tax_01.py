#program to calc net_salery from gross_salery




#inputs
emp_gross_salary = 7000




#prpcessing

if emp_gross_salary >= 5000:
    tax = 10
else:
    tax = 0

emp_net_salary = emp_gross_salary - tax / 100 * emp_gross_salary


#outputs
print(emp_net_salary)
