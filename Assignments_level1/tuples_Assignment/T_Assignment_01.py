ips_List = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.15', 'y'),
    ('192.168.0.11', 'y')
]
unique_list = []

for item in ips_List:
    if item not in unique_list:
        unique_list.append(item)


ips_List = unique_list
print(ips_List)