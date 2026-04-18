length = 8
a = 0
b = 1
term = 0
while term < length:
    print(a,end=" ")
    c = a + b
    a = b
    b = c
    term += 1