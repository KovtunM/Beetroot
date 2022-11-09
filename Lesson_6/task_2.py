stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
list_sum = []
for item in stock:
    total = prices[item] * stock[item]
    list_sum.append(total)
print(list_sum)
print(sum(list_sum))
