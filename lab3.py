'''
i = 0
while i < 20:
    print("rarar")
    i = i+1

for i in range(0, 5):
    print("Hi!")

a = []
for i in range(0, 5):
    a.append("шу")

for i in range(0, 5):
    print(a[i])

a = []
for i in range(0, 5):
    b = input()
    a.append(b)
print(a)
'''
from random import randrange 
from random import randint

for i in range(0, 20):
    a = random.randint(1, 20)
    print(a)
'''
a = randrange(30, 40, 4)
print("I'm ", a, " year old!")

a = [11, 29, 33, 47, 53, 61]
print(random.choice(a))

a = ['я', "люблю", "спать", 'и', "кушать"]
for i in enumerate(a):
    print(i)

    первая задача:
a = 10
b = 20
for i in range(10, 20+1):
    print(i)

    вторая задача:
a = 10
b = 34
if (a > b):
    for i in range(b, a+1):
        print(i)
else:
    for i in range(a, b+1):
        print(i)

    третья задача:
a = 23
b = 1
for i in range(a-(a+1) % 2, b-b%2, -2):
    print(i)

    четвертая задача:
n=5
sum=0
for i in range(1, n+1):
    sum += i
for i in range(n-1):
    sum -= int(input())
print('res: ', sum)
'''

