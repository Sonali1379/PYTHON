'''a = 10
def test():
    a = 20
    print(a)
print(a)
test()
print(a) 
'''
a = 10
def test():
    global a
    a = 20
    print(a)
print(a)
test()
print(a)    