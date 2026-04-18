l = [10,20,30,40,50]
'''k = []
def square(a):
    return a*a

for i in l:
    sq = square(i)
    k.append(sq)
print(k)

k = map(square,l)
'''
k = map(lambda a:a*a,l)
print(list(k))
#- - - - - - 
a = [10,20,30,40,50]
b = [1,2,3,4,5]

k = map(lambda x,y : pow(x,y) ,a,b)
print(list(k))


#- - - - -
sub = ["Python","Java","C++","JavaScript"]
k = map(lambda x : len(x),sub)
print(list(k))


# --------
s = [1,8,27,64,125]
k = map(lambda x : pow(x,(1/3)),s)
print(list(k))