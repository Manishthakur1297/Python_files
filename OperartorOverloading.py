class Emp:

    def __init__(self, name, age, salary):
        self.name = name;
        self.age = age;
        self.salary = salary

    def __str__(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Salary : ",self.salary)
        return " ";

    def __add__(obj1, obj2):
        x  = obj1.salary
        y = obj2.salary
        z = x+y;
        e3 = Emp("Total Salary : ",30,z)
        return e3

##    def __gt__(obj1, obj2):
##        if(obj1.age>obj2.age):
##            return obj1.name + " is Senior"
##        else:
##            return obj2.name + " is Senior"


def __lt__(s, num):
    print("HELLO")
    x = s[int(num):]
    return x;
    
def __gt__(s, num):
    print("HELLO")
    x = " "*int(num)+s[:len(s)-int(num)]
    return x;
    

e1 = Emp("Sushil Verma", 50, 20000)
e2 = Emp("Rashii Verma", 45,40000)
e3 = Emp("Shubham Verma", 21, 10000)

print(e1)
print(e2)
print(e3)

e4 = e1+e2+e3;
print(e4)

##print(e1>e2)
##print(e2>e3)
##print(e3<e1)

s1 = "Hello"
print(s1<str(2))


s2 = "Hello"
print(s2>str(2))
