'''
        *
      * *
    * * *
  * * * *
* * * * *
'''
lines = 5
for i in range(lines):
    for k in range(lines - i-1):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()