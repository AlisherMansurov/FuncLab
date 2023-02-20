'''
def func1(a):
    print("FUNC1")
    for i in range(0, 4):
        b = input()
        a.append(b)

def func2(a):
    print("FUNC2")
    for i in a:
        print(i)

def func3(a):
    print("FUNC3")
    r = []
    for i in range(0, 2):
        b = input()
        r.append(b)
    a.append(r)


a=[]
func1(a)
func2(a)
func3(a)
a.reverse()
a.pop()
'''
def Task1():
    a = []
    m = []
    f = []
    for i in range(0, 8):
        b = input()
        a.append(b)
    for i in range(1, 8, 2):
        if a[i] == "Mat":
            m.append(a[i-1])
            m.append(a[i])
        elif a[i] == "Fiz":
            f.append(a[i-1])
            f.append(a[i])
    a=[]
    a.append(m)
    a.append(f)
    print(a)

def Task2():
    a = ["Vova",["Mat", "Fiz", "His"], [4,4,5], "Malika", ["Mat", "His"], [4,4], "Alisher",["Mat", "Fiz"],[5,5]]

    r = True

    while True:
        b = input("Name of student: ")
        if b == "0":
            break
        else:
            print("Dis: ", a[a.index(b)+1], "Points: ", a[a.index(b)+2])
        
def Task3():
    a=[]
    while True:
        r = int(input())
        if r == 0:
            break
        else:
            a.append(r)
    a.sort()
    for i in a:
        print(i)


def Task4():
    a=[]
    while True:
        r = int(input())
        if r == 0:
            break
        else:
            a.append(r)
    a.sort()
    a.reverse()
    for i in a:
        print(i)

import random
import collections

def Task5():
    a=[]
    for i in range(0, 6):
        b = int(input())
        a.append(b)

    s = 0
    a2 = []
    while True:
        for i in range(0, 6):
            b = random.randint(1, 9)
            a2.append(b)
        if collections.Counter(a2) == collections.Counter(a):
            print("You Won!")
            print(s)
            break
        else:
            a2 = []
            s+=1


def Task6():
    a=[]
    s = 0
    for i in range(0, 6):
        b = input()
        a.append(b)

    if a[0] > a[1]:
        for i in range(0, 5):
            if a[i] < a[i+1]:
                print("not sorted!")
                break
            else:
                s+=1   
        if s==5:
            print("sorted!")
    if a[0] < a[1]:
        for i in range(0, 5):
            if a[i] > a[i+1]:
                print("not sorted!")
                break
            else:
                s+=1   
        if s==5:
            print("sorted!")

Task6()