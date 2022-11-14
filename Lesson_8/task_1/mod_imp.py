from mod_def import name
print('\nPlease enter your details.')
first = input('\nPlease enter your first name: ')
last = input('\nPlease enter your last name: ')
full_name = name(first, last)
print(f'\nHello {full_name}.')
