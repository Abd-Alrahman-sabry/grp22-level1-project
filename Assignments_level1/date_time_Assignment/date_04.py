from datetime import datetime

dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 8, 15),
    datetime(2023, 8, 15),
    datetime(2023, 5, 1)
            ]
given_date = datetime(2023, 8, 15)

count_date = 0
for date in dates_list:
    if date == given_date:
        count_date = count_date + 1


print(given_date.date(), 'occurs', count_date,  'times')
