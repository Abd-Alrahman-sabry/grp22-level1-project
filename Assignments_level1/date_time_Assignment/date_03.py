from datetime import datetime
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
given_date = datetime(2023, 6, 15)

if start_date < given_date < end_date:
    print('The date is in range')
else:
    print('The date is out of range')
