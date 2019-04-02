def abc():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 11
    yield 12


collection  = abc()

for i in collection:
    print(i)
print("\n")

def cube():
    for i in range(1,11):
        num = i**3
        yield num

cb = cube();

for i in cb:
    print(i)
