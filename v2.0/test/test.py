import pdb

def f():
    a = [1]
    return a

a = [1,2]
f()
print(a)
print(f())
a = f()
print(a)
