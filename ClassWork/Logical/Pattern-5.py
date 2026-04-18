'''
* * * * *
  * * * *
    * * *
      * *
        *
'''
lines = 5
for i in range(lines):
    for k in range(i):
        print(" ", end=" ")
    for j in range(lines - i):
        print("*", end=" ")
    print()