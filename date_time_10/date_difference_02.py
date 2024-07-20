# program to get the difference between 2 dates
from datetime import datetime

from dateutil.relativedelta import relativedelta


today = datetime.today()
custom_date = datetime(year=2021, month=4, day=17)
print('today = ', today)
print('custom_date = ', custom_date)


difference_in_days = today - custom_date
print(difference_in_days)
print(difference_in_days.days)

print('-----------')
difference_parts = relativedelta(today, custom_date)
print(difference_parts)
print('difference in years = ', difference_parts.years)
print('difference in months = ', difference_parts.months)
print('difference in days = ', difference_parts.days)
