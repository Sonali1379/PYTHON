number = 153
temp = number
sum = 0
while number != 0:
    rem = number % 10
    sum +=pow(rem,3)
    number //= 10
if temp == sum:
    print(f"{temp} is an armstrong number")
else:
    print(f"{temp} is not an armstrong number")