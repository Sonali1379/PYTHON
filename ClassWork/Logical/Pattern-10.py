''' 1
    2 3
    4 5 6
    7 8 9 10
'''
lines = 4
num = 1
for i in range(lines):
    for j in range(i+1):
        print(num, end=" ")
        num += 1
    print()