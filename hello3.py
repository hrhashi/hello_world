#while True:
#    try:
#        x = int(input("Enter a number: "))
#        print("ok")
#        break
#    except ValueError:
#        print("Try again!")

import sys

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")

print(sys.exc_info())

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    x, y = inst.args
    print(type(x))