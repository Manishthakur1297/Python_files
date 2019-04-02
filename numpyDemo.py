from numpy import *;
class Abc:
    pass


arr = array([],Abc)

print(arr.dtype)
print(arr)

ls = linspace(1,50,100)
print(ls)

logs = logspace(1,50)
print(logs[1])
print("%.1f" %logs[49])

ar = arange(1,50,5)
print(ar)

z1 = zeros(10,int)
print(z1)


z1 = zeros(10,bool)
print(z1)

z1 = ones(10,int)
print(z1)

z1 = ones(10,bool)
print(z1)

arr1 = array([1,2,3,4,5],int)
arr2 = arr1.view()
arr1[0] = 0
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))


arr3 = array([1,2,3,4,5],int)
arr4 = arr3.copy()
arr3[0] = 0
print(arr3)
print(arr4)
print(id(arr3))
print(id(arr4))

