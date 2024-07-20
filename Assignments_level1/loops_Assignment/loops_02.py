lst = []
for i in range(1500, 2700):
    if i % 7 == 0 and i % 5 == 0:
        lst.append(i)


for i in range(len(lst)):
    if lst[i] < lst[-1]:
        print(lst[i], end=',')
    elif lst[i] == lst[-1]:
        print(lst[i])
