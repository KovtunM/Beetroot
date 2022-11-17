def input_number():
    try:
        a = int(input('Enter the first number: '))
        b = int(input('Enter the second number: '))
        print(a * 2 / b)
    except ZeroDivisionError as error_1:
        print(error_1)
    except ValueError as error_2:
        print(error_2)


input_number()
