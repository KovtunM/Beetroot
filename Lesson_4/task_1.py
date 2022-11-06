import random
print('Let\'s play the game "Guess the random number"!')
random_number = int(random.randint(1, 10))
player = int(input('Enter a number from 1 to 10: '))
res_1 = random_number
res_2 = player
if res_1 > res_2:
    print(f'You did not guess, you entered: {res_2}, random number: {res_1}.')
elif res_1 < res_2:
    print(f'You did not guess, you entered: {res_2}, random number: {res_1}.')
else:
    res_1 = res_2
    print(f'You guessed it, you entered: {res_2}, random number: {res_1}.')
