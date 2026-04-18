'''
        *
      * *
    * * *
  * * * *
* * * * *
'''
lines = 5
star = 1
space = lines - 1
for i in range(lines):
    for k in range(space):
        print(" ", end=" ")
    for j in range(star):
        print("*", end=" ")
    star += 1
    space -= 1
    print()