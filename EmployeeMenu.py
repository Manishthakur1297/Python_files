def create():
    name = input("Enter Name : ");
    age = int(input("Enter Age : "));
    salary = int(input("Enter Salary : "));
    designation = input("Enter Designation : ");
    f = open("employee.txt", "a");
    f.write(name+"|"+str(age)+"|"+str(salary)+"|"+designation+"\n");
    f.close();

def display():
    f = open("employee.txt", "r");
    for line in f:
        arr = line.split("|");
        print("-"*30)
        print("Name : "+arr[0]+"\nAge : "+arr[1] + "\nSalary : "+arr[2] + "\nDesignation : "+arr[3])
        print("-"*30)
    f.close();

while(True):
    print("-"*30)
    print("1. Create")
    print("2. Display")
    print("3. Exit")
    print("-"*30)
    choice = int(input("Enter Choice : "))
    if(choice==1):
        create()
    elif(choice==2):
        display()
    else:
        break;
    
