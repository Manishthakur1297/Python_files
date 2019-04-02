class Emp:
    count=0;
    def __init__(self,name,age, salary, desig):
        self.name = name;
        self.age = age;
        self.salary = salary;
        self.desig = desig
        Emp.count+=1;

    def display(self):
        print("Name : ", self.name);
        print("Age : ", self.age);
        print("Salary : ", self.salary);
        print("Desig : ", self.desig);
        

e1 = Emp("Manish",21,100000,'CLerk')
e1.display()
Emp.count;
