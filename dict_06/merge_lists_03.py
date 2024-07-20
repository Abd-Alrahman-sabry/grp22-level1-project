# program to merge 2 lists into a dictionary
emp_ids_list = [101, 102, 103]
emp_names_list = ['Ahmed', 'Omar', 'Sarah']

# create empty dictionary
person_dict = {}



# loop over emp_ids_list using for i index loop
for i in range(len(emp_ids_list)):
    person_dict[emp_ids_list[i]] = emp_names_list[i]    # fill



print(person_dict)