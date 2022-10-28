first_name = 'mykhailo'
last_name = 'kovtun'
full_name = first_name + ' ' + last_name
s = 'hello'
a = first_name
a2 = last_name
initials = first_name[0]+last_name[0]
print(s.title() + ' ' + first_name.title() + ' ' + last_name.title())
print(f'{s.title()} {first_name.title()} {last_name.title()}')
print(f'{s.title()} {full_name.title()}')
print(s.title() + ' ' + full_name.title())
print(s.title() + ' ' + first_name.title() + '.' + last_name[0].title())
print(first_name.title() + ' ' + initials[0].title()+initials[1].title() + ' ' + last_name.title())
print(f'{s.title()} {a.title()} {a2.title()}')
