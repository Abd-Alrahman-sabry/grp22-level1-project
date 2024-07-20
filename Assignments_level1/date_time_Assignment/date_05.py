from datetime import datetime


def check_dates(dates_list):
    for i in range(len(dates_list)):
        if dates_list[0].month != dates_list[i].month:
            return False
    return dates_list[0].month


dates_list_test = [
    datetime(2023, 12, 31),
    datetime(2023, 12, 15),
    datetime(2023, 12, 15),
    datetime(2023, 12, 1)
]
month = check_dates(dates_list_test)

if not month:
    print('All dates are not in the same month ')
else:
    print('All dates are in the same month : ', month)
