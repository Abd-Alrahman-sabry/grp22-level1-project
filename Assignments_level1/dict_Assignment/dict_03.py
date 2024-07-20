print('--------------Example library-------------')
book_dict = {'pages': '277', 'name': 'Gone Girl', 'year': 2007}
print(book_dict)
print('-----------Adding Elements To a Dictionary-------------')
book_dict['Author'] = 'Well Max'
print(book_dict)
print('-----------Accessing Elements inside a Dictionary-------------')
print(book_dict['name'])
print('--------------Changing Elements inside a Dictionary-------------')
book_dict['year'] = '2010'
print(book_dict)
print('-----------using loop to print keys and values-------------')
for key, value in book_dict.items():
    print(key, value)


print('-----------Removing items from a Dictionary-------------')
book_dict.pop('name')
print(book_dict)