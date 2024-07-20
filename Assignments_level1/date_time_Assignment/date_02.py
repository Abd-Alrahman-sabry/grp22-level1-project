from datetime import datetime
given_date = datetime(2023, 8, 15)
dates_list = [datetime(2023, 12, 31), datetime(2023, 8, 15), datetime(2023, 5, 1)]

for i in range(len(dates_list)):
    if given_date.date() == dates_list[i].date():
        print(given_date.date(), 'is found in the list at index ', i)
