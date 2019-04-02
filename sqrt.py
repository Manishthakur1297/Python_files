import math

def checkPerfect(num):
    sq = math.sqrt(num);
    if(math.floor(sq)==sq):
        return True;
    return False;

l = []
n = int(input("Enter value of n : "))
for i in range(1,n+1):
    num = int(input("Enter number "+ str(i) + " : "))
    if(checkPerfect(num)):
        l.append(num)
for i in l:
    print(i)
