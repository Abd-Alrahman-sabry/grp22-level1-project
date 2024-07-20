# program to go to a specific day in a date
import calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
print(today)

print('-----Go to the first day in the month-----')
first_date = today + relativedelta(day=1)
print('first date:', first_date)

print('-----Go to the last day in the month-----')
last_date = today + relativedelta(day=31)
print('last day:', last_date)

# task
print('-----Go to the last day in the next month-----')
last_date_02 = today + relativedelta(day=31, months=1)
print('last date:', last_date_02.date())


print('-----the nearst sunday from today----')
nearst_sunday = today + relativedelta(weekday=calendar.SUNDAY)
print('nearst sunday:', nearst_sunday)

print('-----the nearst 2nd sunday from today----')
nearst_2nd_sunday = today + relativedelta(weekday=calendar.SUNDAY, weeks=1)
print('nearst 2nd sunday:', nearst_2nd_sunday)
