ips_List = [

    ('192.168.0.15', 'y'),

    ('192.168.0.22', 'y'),

    ('192.168.0.14', 'y'),

    ('192.168.0.24', 'n'),

    ('192.168.0.15', 'y'),

    ('192.168.0.11', 'y')

    ]


duplicate_list = []
for i in range(len(ips_List)):
    if ips_List[i] not in duplicate_list:
        duplicate_list.append(ips_List[i])


ips_List = duplicate_list
print(ips_List)