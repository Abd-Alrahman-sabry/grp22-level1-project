# Here we will show all basic operations on datetime
from datetime import datetime  # from module datetime import class datetime
print('---- Get the current date and time -----')
today = datetime.now()
print(today)

print('---- get only date or time or their parts -------')
print(today.date())
print(today.date().year)
print(today.date().month)
print(today.date().day)
print(today.date().weekday())

print(today.time())
print(today.time().hour)
print(today.time().minute)
print(today.time().second)


print('---- Re Formatting date, time --- | we use strftime() function----')
print('----- Convert date into string using strftime() function -----')
# day, month, year,yr,weekday, week no per Year
print(today.strftime('%d-%m-%Y'))
print(today.strftime('%d-%m-%Y   %y  %w %W'))


# Month, Mon, Day, Dy
print(today.strftime('%B-%b-%A-%a'))

# Hours in 24 hours style
print(today.strftime('%H:%M:%S'))


# Hours in 12 hours style
print(today.strftime('%I:%M:%S  %p'))


print('---------------- Create a custom date : 24-04-2023 ------------')
print('-- 1st way : datetime object using constructor ( ) ')
custom_date = datetime(year=2023, month=4, day=24)
print(custom_date)



print('--- 2nd way - by converting a string to Date using strptime() function -----')
data_style_string = '24-4-2023'
new_custom_date = datetime.strptime(data_style_string, '%d-%m-%Y')
print(new_custom_date)



print('----------- Comparison ------------')
if today.date() > custom_date.date():
    print('Today is newer than custom date')
elif today.date() < custom_date.date():
    print('Today is older than custom date')
else:
    print('Today is equal to custom date')