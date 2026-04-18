l = [4,5,7,8,9,40,6,13,17]
# c = []

# def checkeven(a):
#     if a%2==0:
#         return a
    
# for i in l:
#     k = checkeven(i)
#     if k is not None:
#        c.append(k)
# print(c)

# c = filter(checkeven,l)
c = filter(lambda k : k%2==0 ,l)
print(list(c))
'''sub = ["python","Java","php","node","android"]
k = filter(lambda x : x.startswith("p"),sub)
print(list(k))
'''
'''l = [2,5,9,8,25,49,45,81,144,22,33]
k = filter(lambda x : x**(0.5) % 1 == 0,l)
print(list(k))
'''