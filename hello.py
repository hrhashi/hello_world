

def func1(**args):
    for a in args:
        print(a, args[a])

#func1(arg1="aaa", arg2="bbb", arg3="ccc")

def func2(*arg) -> None:
    """Oh no!"""
    for a in arg:
        print(a)

#func2(1,2,3,4)
#print(func2.__annotations__)

arg = [10,20,30]

pairs = [(0, "zero"), (1,"one"), (2, "two"), (3, "three"), (4, "four")]

#pairs.sort(key=lambda pair: pair[1])
#print(pairs)

t = (1,2,[4,6,7])
t += (4, )
a, b, c, d = t
#print(a, b, c, d)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana', 'banana']
#print(basket)
#print('car' in basket)

a = set('abracadabra')
b = set('alacazam')
#print(a)
#print(b)
#print(a - b)
#print(a & b)
#print(a ^ b)

c = {x  for x in a if x not in 'abc'}
#print(c)


ll = [6,7,8,3,5,7,9,9]
a = set(ll)
#print(a)

tel = {'Tom': 4044, 'Mary': 5002, 'Jack': 6007}
#print(tel)
#print(list(tel.keys()))
#print(sorted(tel.keys()))
#tel['Mary'] = 9001
#print(tel)
#print('Thomas' in tel)
#print('Mary' in tel.keys())

d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098), ('guido', 6000)])
#print(d.items())

#for k, v in d.items():
#    print(k, v)

#for i, p in enumerate(d):
#    print(i, p, d[p])

d = {x: x**2 for x in [1,2,3,7, 0.5]}
print(d)


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

for i in reversed(range(10)):
    print(i)

for fruit in sorted(basket):
    print(fruit)
print('-' * 10)
for fruit in basket:
    print(fruit)
print('-' * 10)

c1 = [1,2,3]
c2 = [1,2,3,4]
print(c1 == c2)

