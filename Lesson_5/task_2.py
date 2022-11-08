import random
list_1 = []
list_2 = []
list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_4 = []
for i in range(10):
    list_2.append(random.randint(1, 10))
    list_1.append(random.randint(1, 10))
    for item in list_3 and list_2:
        if item == i in list_1:
            list_4.append(i)
print(list_1)
print(list_2)
print(list_4)
