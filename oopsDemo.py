class Emp:


    
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
    
    def display(self) :
        print("Name : "+self.name);
        print("Age : "+self.age);



##e1 = Emp("Manish", "21");
##Emp.display(e1);
##e1.display();


class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        print("Add Result : ",a+b)



c1 = Calculator();
Calculator.add(c1,10,20)
c1.add(10,30);
