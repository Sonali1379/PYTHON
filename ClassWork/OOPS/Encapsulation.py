class Test:
    a = 10
    _b = 20
    __c = 100

    def set(self, a):
        self.__c = 0

    def get(self):
        return self.__c
    
    def test(self):
        print(self.a, self._b, self.__c)


class Demo:
    def disp(self):
        print(self._b)

t = Test()
t.set(500)
print(t.get())


#print(dir(t))
# print(t.a)
# print(t._b)
# print(t._Test__c)