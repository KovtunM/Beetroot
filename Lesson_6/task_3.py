i = tuple(range(1, 10))
list_1 = [i]

for item in i:
    item *= item
    list_1.append(item)
print(list_1)
