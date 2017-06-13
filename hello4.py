import math

class MyClass:
    """Simple Class"""

    instances = 0

    def __init__(self, n):
        self.data = n
        self.instances += 1

    def func(self):
        return self.data


x = MyClass(689)
x.l = [3,5,6]
print(x.l)

y = MyClass(700)
y.l = [8,9,0]
print(x.l)

f = x.func
print(f())

f = MyClass.func
print(f(y))

print(issubclass(bool, int))
print(isinstance(x, MyClass))