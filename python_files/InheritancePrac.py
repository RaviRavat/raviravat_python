class A:
    def getA(self,a):
        self.a=a
    def getA(self):
        print("A:",self.a)

class B:
    def getB(self,b):
        self.b=b
    def put(self):
        print("B:",self.b)
class C(B):
    def getC(self,c):
        self.c=c
    def put(self):
        print("C:",self.c)
b1=A()
b1.getA(10)
b1.getB(20)
b1.getC(30)              
b1.putA()
b1.putB()
b1.putC()
