octal = '574566'
sum = 0
power = 0
    
while octal!=0:
    rem = octal%10
    sum += rem*pow(8,p)
    octal //= 10
    p += 1

print(sum)