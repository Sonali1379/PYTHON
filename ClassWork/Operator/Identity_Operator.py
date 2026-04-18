#identity : is , is not

a = [10,20,30]
b = [10,20,30]
c = a
print(a)
a.append(400)
print(a)
print(b)


print(a is c)
print(a is b)
print(a is not b)