number = 12321
temp = number
rev = 0
while number != 0:
    rem = number % 10
    rev = rev * 10 + rem
    number //= 10
if temp == rev:
    print(f"{temp} is a pelindrom number")
else:
    print(f"{temp} is not a pelindrom number")