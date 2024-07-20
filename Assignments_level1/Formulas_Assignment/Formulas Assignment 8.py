import math



loanAmount = 100000
monthlyInterestRate = 0.01
noYears = 7


monthly_payment = round(((loanAmount * monthlyInterestRate) / (1- (1/ math.pow(1+monthlyInterestRate, noYears * 12)))), 2)

total_payments = round((monthly_payment * noYears * 12), 2)



print('monthly payment = ' + str(monthly_payment))
print('total payment = ' + str(total_payments))

print('monthly payment = ', monthly_payment)