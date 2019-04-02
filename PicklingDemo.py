import pickle;
from Person import Person;

p1 = Person("Manish", 21)
p2 = Person("MJ", 22)
f1 = open("person.ser", "wb")
pickle.dump(p1,f1)
pickle.dump(p2,f1)
f1.close()

print("Pickkle Successfully")
