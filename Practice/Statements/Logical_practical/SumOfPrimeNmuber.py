sum = 0
for j in range(2, 101):
    flag = 0
    for i in range(2, j):
        if j % i == 0:
            flag = 1
            break
    if flag == 0:
        sum = sum + j
print(f"The sum of prime numbers between 1 and 100 is {sum}")