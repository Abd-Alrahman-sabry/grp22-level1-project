# program to count fridays, or saturdays in a specific month
from datetime import datetime
from dateutil.relativedelta import relativedelta


# inputs
the_year = 2024
the_month = 8


# processing
custom_date = datetime(year=the_year, month=the_month, day=1)
end_date = custom_date + relativedelta(months=1)

weekend_counter = 0
while custom_date < end_date:
    if custom_date.date().weekday() in (5, 4):
        weekend_counter += 1
    custom_date = custom_date + relativedelta(days=1)


print('Weekend counter:', weekend_counter)
