s = [(10,'Python'),(20,'java'),(30,'php'),(40,'android')]
t = zip(*s)
print(next(t))
print(next(t))
print(list(t))


# t = zip(s)
# # print(next(t))
# # print(next(t))
# print(list(t))