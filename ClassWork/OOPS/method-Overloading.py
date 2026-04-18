from multipledispatch import dispatch
class clac :
    @dispatch(int, int, int)
    def add(self, a, b, c):
        print("Addition of 3 numbers is ", a+b+c)
    @dispatch(int, int)
    def add(self, a, b):
        print("Addition of 2 numbers is ", a+b)




# def add(self,*a):
#     sum = 0
#     for i in a:
#         sum = sum + i
#     print(sum)


c = clac()
c.add(10,20,30)
c.add(10,20)