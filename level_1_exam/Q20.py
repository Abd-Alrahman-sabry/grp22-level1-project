string_01 = 'love python more love java'
string_lst = string_01.split()
count_word = 0
for word in string_lst:
    if word == 'love':
        count_word += 1

print('love showed times = ', count_word)
