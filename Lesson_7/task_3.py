def make_number():
    num_1 = int(input('Перше число: '))
    num_2 = int(input('Друге число: '))
    num_3 = int(input('Третє число: '))
    num_4 = int(input('Четверте число: '))
    operator = input('Арифметичний оператор " +, -, *, / ": ')
    if operator == '+':
        print(num_1 + num_2 + num_3 + num_4)
    elif operator == '-':
        print(num_1 - num_2 - num_3 - num_4)
    elif operator == '/':
        if num_2 or num_3 or num_4 == 0:
            print('Ділення на "0" неможливе!')
        else:
            print(num_1 / num_2 / num_3 / num_4)
    elif operator == '*':
        print(num_1 * num_2 * num_3 * num_4)


make_number()
