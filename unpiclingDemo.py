import pickle;
from Person import Person;

f2 = open("person.ser", "rb")
p1 = pickle.load(f2)
print(p1)

p1 = pickle.load(f2)
print(p1)
print(p1.name)
print(p1.age)
f2.close()

print("UnPickkle Successfully")
