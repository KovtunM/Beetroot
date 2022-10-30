phone_n = '9874640311'

if len(phone_n) == 10 and phone_n.isdigit():
    print("Phone number.")
elif len(phone_n) <= 10 and phone_n.isdigit():
    print("Low numbers!")
elif len(phone_n) >= 10 and phone_n.isdigit():
    print("Too many numbers!")
else:
    phone_n.isalpha()
    print("Invalid format!")
