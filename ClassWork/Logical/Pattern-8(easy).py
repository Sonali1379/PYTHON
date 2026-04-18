'''
    * 
  * * *
* * * * *
  * * * 
    *
'''
lines = 5
star = 1
space = lines - 1
mid = lines // 2
for i in range(lines):
    for k in range(space):
        print(" ", end=" ")
    for j in range(star):
        print("*", end=" ")
    if i < mid:
        star += 2
        space -= 1
    else:
        star -= 2
        space += 1
    print()