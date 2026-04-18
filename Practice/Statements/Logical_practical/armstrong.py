count = 0
for i in range(100,1000):
    sum = 0
    a = i
    while a > 0:
        r = a % 10
        sum = sum + r**3
        a = a // 10
    if sum == i:
        print(f"{i} is an armstrong number")
        count += 1
print(f"There are {count} armstrong numbers between 100 and 1000")