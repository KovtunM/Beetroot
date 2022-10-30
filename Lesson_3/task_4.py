name = 'Vlad'
if name.title():
    print(name)
elif name.lower():
    print(name)
else:
    name.upper()
    print(name)


name = input("What is your name?:")
if name.title():
    print("Hello" + ' ' + name)
elif name.lower():
    print("Hello " + name)
else:
    name.upper()
    print(f"Hello {name}")
