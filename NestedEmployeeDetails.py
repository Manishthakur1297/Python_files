class Emp:
    def __init__(self, name, age, state, city, pin):
        self.name = name;
        self.age =age;
        self.addr = Address(state, city, pin)
        self.computer = self.Computer("HP", "FC4750", "Intel i8", "2.2Ghz","16GB");

    def display(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        self.addr.display();
        self.computer.display();


    class Computer:
        def __init__(self, brand, model, processor, speed, ram):
            self.brand = brand;
            self.model = model;
            self.processor = processor;
            self.speed = speed
            self.ram = ram;

        def display(self):
            print("Company : ",self.brand);
            print("Model : ",self.model);
            print("Processor: ",self.processor);
            print("Clock Speed : ",self.speed);
            print("RAM: ",self.ram);


class Address:
    def __init__(self, state, city, pin):
        self.state = state;
        self.city = city;
        self.pin = pin;

    def display(self):
        print("State : ",self.state);
        print("City : ",self.city);
        print("Pincode: ",self.pin);



e = Emp("Manish",21,"Karnataka","Bengaluru",560032)
e.display();
