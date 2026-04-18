'''
    * 
  * * *
* * * * *
  * * * 
    *
'''
lines = 3
for i in range(lines):
    for k in range(lines - i-1):
        print("  ", end="")
    for j in range(2 * i + 1):
        print("* ", end="")
    print()

for i in range(lines):
    for k in range(i+1):
        print(" ",end="")
    for j in range(((lines-(i+1))*2)-1):
        print(" *",end="")
    print()