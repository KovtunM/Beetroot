import random
word = input('Word: ')
for i in range(5):
    result = ''.join(random.sample(word, 5))
    print(result)
