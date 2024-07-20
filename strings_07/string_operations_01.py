# show strings functions
print('---- Create and print string ----')
emp_name = 'Yahia Momtaz'
print(emp_name)
print(type(emp_name))



print('-------- upper(), lower() functions -------------')
upper_emp_name = emp_name.upper()
lower_emp_name = emp_name.lower()
print(emp_name)
print(upper_emp_name)
print(lower_emp_name)


print('------ isupper(), islower(), isalpha() functions --- True , False --')
print(upper_emp_name.isupper())  # True
print(lower_emp_name.islower())  # true
print(emp_name.isupper())  # false
print(emp_name.isalpha())  # false
emp_code = '1001'
print(emp_code.isdigit())
emp_code = '1001abc'
print(emp_name.isalnum())
emp_sign = '+-!@'
print(not emp_sign.isalnum())


print('-------------- endsWith() function -----------------')
file_path = 'c:/MyDocuments/egypt.Jpg'
file_path = file_path.lower()  # ignore case sensitive
if file_path.endswith('pdf'):
    print('It is a book')
elif file_path.endswith('jpg') or file_path.endswith('png'):
    print('It is an image')
elif file_path.endswith('mp4'):
    print('It is a video')
else:
    print('unknown type')






print('-------------- startswith() function ---------')
emp_mobile = '01521456870'
if emp_mobile.startswith('010'):
    print('It is a Vodafone number')
elif emp_mobile.startswith('011'):
    print('It is a Etisalat number')
elif emp_mobile.startswith('012'):
    print('It is a Orange number')
else:
    print('unknown network')


print('------ in membership --------------')
emp_cv = 'iam a programmer, iam interested in python, java, c++'
if 'python' or 'java' in emp_cv:
    print('This is the wanted employee')
else:
    print('This is not the wanted employee')





print('-------------- count function -----------')
emp_cv = 'iam a python programmer, iam interested in python, java, c++'
print(emp_cv.count('python'))
# loop over string words



print('---------- index(),  replace() functions |  slicing---------------')
emp_email = 'aly.momtaz.mohamed@gmail.com'
user_name = emp_email[0: emp_email.index('@')]
print(user_name)
domain_name = emp_email[emp_email.index('@') + 1:]
print(domain_name)
real_name = user_name.replace('.', ' ')
print(real_name)




print('--------------- Looping :  Loop over letters of string -----------------------')
emp_email = 'yahia.momtaz@gmail.com'
print('-------------1. loop using for i loop index------------')
for i in range(len(emp_email)):
    print(emp_email[i])

print('-------------2. loop using for each loop ------------')
for letter in emp_email:
    print(letter)




print('------- Split function the String into List of Words -------')
my_courses = 'java python oracle linux php ccna'
courses_list = my_courses.split()  # convert from string to list
print(courses_list)
courses_list.reverse()
courses_list.append('Networking')
print(courses_list)


print('------ return the list back to string using join() function --------')
new_courses = '-'.join(courses_list)  # covert from list to string
print(new_courses)





print('---------- strip(), title(), swapcase(), find(), rfind() Self study   -------------------')
my_courses = '             java python oracle linux php ccnaj    '

my_courses = my_courses.strip()
print(my_courses)
'''''
my_courses = my_courses.title()
print(my_courses)

my_courses = my_courses.swapcase()
print(my_courses)
'''
# my_courses = my_courses.find("j")
print(my_courses)
my_courses = my_courses.rfind("j")
print(my_courses)








