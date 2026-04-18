'''
      *
    * * *
  * * * * *
* * * * * * *
'''
lines = 4
for i in range(lines):
    for k in range(lines - i-1):
        print("  ", end="")
    for j in range(2 * i + 1):
        print("* ", end="")
    print()