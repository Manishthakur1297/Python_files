f1 = open("abc.txt", "r")

#print(f1.read())

print(f1.readline(),end="")
print(f1.readline())
print(f1.readline())

#f1.close();


#f2 = open("xyz.txt","w");
#f2.write("Hi from write mode");
#f2.close();

f3 = open("xyz.txt","a");
f3.write("\nThank you");
f3.close();
f1.seek(0);
f4 = open("xyz.txt","a");
for data in f1:
    f4.write(data)
f4.close();
f1.close();

f5 = open("background.jpeg", "rb")
#print(f5.read());

f6 = open("background_copy.png", "wb")
for data in f5:
    f6.write(data)
f5.close();
f6.close();
