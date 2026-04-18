l = [10,20,30,40,50,60]
from functools import reduce
'''def max(x,y):
    if x>y:
        return x
    else:
        return y
        '''
# def add(a,b):
#    print(a,b)
#    return a+b

r = reduce(lambda a,b:a+b,l)
print(r)
#- - - - - -
k = reduce(lambda x,y : max(x,y),l)
print(k)