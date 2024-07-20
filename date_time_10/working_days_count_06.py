# program to get the date after 12 working days from a date
from datetime import datetime
from dateutil.relativedelta import relativedelta

today = datetime.now()
jump_working_days = 12

require_date = today
for i in range(jump_working_days):
    if require_date.date().weekday() == 3:
        require_date = require_date + relativedelta(days=3)
    elif require_date.date().weekday() == 4:
        require_date = require_date + relativedelta(days=2)
    else:
        require_date = require_date + relativedelta(days=1)

print('The target date = ', require_date)


