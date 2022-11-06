div_7 = []
div_5 = []

for i in range(1, 101):
    if i % 7 == 0 and i % 5 != 0:
        div_7.append(i)
    elif i % 5 == 0:
        div_5.append(i)
print(div_7)
print(div_5)






