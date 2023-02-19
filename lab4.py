'''
def Str1():
    print("Function1")
    print("My name is Alisher")

def Str2(name, age):
    print("Function2")
    print("My name is", name, "\n I'm", age, " years old")

def Str3(name, age):
    print("Function3")
    if age < 18:
        print(name, " can't drive")
    else:
        print(name, " can drive")

def Str4(number):
    print("Function4")
    a1 = int(number[0])+ int(number[1])
    a2 = int(number[2])+ int(number[3])
    if a1 == a2:
        print(number, " is happy number")
    else:
        print(number, " isn't happy number")

def Str5(day_of_week):
    print("Function5")
    match day_of_week:
        case "Monday":
            print("will be -4")
        case "Tuesday":
            print("will be -5")
        case "Wednesday":
            print("will be -3")
        case "Thursday":
            print("will be -7")
        case "Friday":
            print("will be -8")
        case "Saturday":
            print("will be -6")
        case "Sunday":
            print("will be -2")
    
def Str6(s1, s2):
    print("Function6")
    print(s1 + s2)

def Str7(s1):
    print("Function7")
    print(s1 * 4)

def Str8(s2):
    print("Function8")
    print(len(s2))

def Str9(s1):
    print("Function9")
    for i in s1:
        print(i)

def Str10(s1):
    print("Function10")
    print(s1[1:len(s1)-1])

name = "Alisher"
age = 20
number = "1212"
day_of_week = "Tuesday"
s1 = "house"
s2 = "dog"

Str1()
Str2(name, age)
Str3(name, age)
Str4(number)
Str5(day_of_week)
Str6(s1, s2)
Str7(s1)
Str8(s2)
Str9(s1)
Str10(s1)
'''

'''
def Classes():
    a = []
    for i in range(0, 10): #2 b 1 a 3 c 5 v 4 d 
        b = input()
        a.append(b)

    for i in range(0, len(a), 2):
        min = a[i]
        index = i
        for j in range(i+2, len(a), 2):
            if min>a[j]:
                min = a[j]
                index = j
        a[index] = a[i]
        temp = a[index+1]
        a[index+1] = a[i+1]
        a[i+1] = temp
        a[i] = min
    print(a)

Classes()
'''

'''
str = input('input: ')
up=0
low=0
r = str.replace(' ', '')
for i in r:
    if i.isupper():
        up+=1
    else:
        low+=1
if up == low:
    str = str.lower()
elif up > low:
    str = str.upper()
else:
    str = str.lower()
print(str)
'''

'''
r = True
while r:
    a = input("a: ")
    if a.isdigit():
        res1 = a
        r = False
    else:
        print("a is not a number")
r = True
while r:
    b = input("b: ")
    if b.isdigit():
        res2 = b
        r = False
    else:
        print("b is not a number")
print("result: ", int(res1)+int(res2))
'''

