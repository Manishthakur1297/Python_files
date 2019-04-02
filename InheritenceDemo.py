class A:
    def abc(self):
        print("A Class")


class B:
    def xyz(self):
        print("B Class")


class C(A,B):
    
    def atoz(self):
        print("THANKS");


class D:
    z = 30;

    def __init__(self):
        pass
    
    @classmethod
    def classMethod(cls):
        print("From Class Method : ",cls.z)


    @staticmethod
    def xyz(s):
        print("This is from static method...", s)
    
    def atoz(self):
        print("THANKS");

        
c = C();
c.abc();
c.xyz();
c.atoz();
print("-----")
d = D()
D.classMethod()
D.xyz("HI");
