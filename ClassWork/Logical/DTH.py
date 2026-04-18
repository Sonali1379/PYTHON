number = 489
sum =""
k = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
while number!=0:
    rem = number % 16
    sum = k[rem]+sum
    number = number//16
print(sum)