class Test:
    def Concate(self,a,b):
        print(a+b)

class Test2(Test):
    def Concate(self,a,b):
        print(a+b)

t1=Test()
t1.Concate(3,4)
t2=Test()
t2.Concate("Hello","Ashrith")
