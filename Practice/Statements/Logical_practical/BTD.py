binary = 10101110101
p = 0
sum = 0
while binary!=0:
    rem = binary % 10
    sum += rem * pow(2,p)
    binary //=10
    p += 1

print(sum)