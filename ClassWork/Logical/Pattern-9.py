'''
  *
 * *
*   *
 * *
  *
'''
lines = 3
for i in range(lines):
    for k in range(lines - i-1):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
lines = 2
for i in range(lines):
    for k in range(i):
        print(" ", end="")
    for j in range(2 * (lines - i) - 1):
        if j == 0 or j == 2 * (lines - i) - 2:
            print(" *", end="")
        else:
            print("", end="")
    print()    