person_list = [{101: 'Omar', 102: 'Esraa', 103:'Ibrahim'}]
print(len(person_list))

# {101: 'Omar', 102: 'Esraa', 103:'Ibrahim'}
print(person_list[0])

# Esraa
print(person_list[0][102])

print('---loop over dict keys | values-----')
for key, value in person_list[0].items():
    print(key)
    print(value)
    print('----')



print('---add new dict to the list----')
students_dict = {104:'Esam', 105:'Ayman', 106: 'Hagar'}
person_list.append(students_dict)
print(person_list)


print(person_list[1][105])