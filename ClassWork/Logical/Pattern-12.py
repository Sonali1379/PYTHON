'''
5
4 5
3 4 5
2 3 4 5
1 2 3 4 5
'''
lines = 5
for i in range(lines):
    for j in range(lines-i,lines+1):
        print(j, end=" ")
    print()