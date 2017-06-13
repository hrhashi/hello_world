import sys
import math

def func(n):
    return n+1

print(sys.path, len(sys.path))

A = {1,2,3}
B = {1,3,5}
C = [x**(1/2) for x in range(5)]
print(A & B)
print(A | B)
print(A ^ B)

ss = "I have {0} {1}."
print(ss.format(2, "pens"))
print("pi = {0:.10f}".format(math.pi))

with open('afo.txt', 'r+') as myfile:
#for line in myfile:
#    print(line, end='')
    mylist = myfile.readlines()
    myfile.writelines("I am a student.")
    value = ("forty two", 42)
    myfile.writelines(str(value))
    print(myfile.closed)
print(myfile.closed)
