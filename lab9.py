from functools import reduce
#1 задание
#def void(mas):
#    print('-'* 10)
#    for i in mas:
#        print(*i)
#    print('-'* 10)
#
#def int1(mas):
#    sum = 0
#    for i in range(0, len(mas)):
#        for j in range(0, len(mas)):
#            sum += mas[i][j]
#    return sum
#
#mas = [
#    [1, 0, 0, 0],
#    [0, 0, 2, 0],
#    [0, 0, 0, 0],
#    [0, 0, 0, 10]
#]
#
#void(mas)
#print(int1(mas))

#2 задание
#def rltd():
#    list = [1, 2, 3, 4, 5]
#    tuple = ('apple', 'banana', 'tomato')
#    dict = {'name': 'Alisher', 'age': 20, 'city': 'Almaty'}
#
#    return list, tuple, dict

#3 задание
#n = [1, 2, 3, 4, 5]
#map_res = list(map(lambda x: x ** 2, n))
#print(map_res)  # [1, 4, 9, 16, 25]
#
#n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#filter_res = list(filter(lambda x: x % 2 == 0, n))
#print(filter_res)  
#
#n = [1, 2, 3, 4, 5]
#reduce_res = reduce(lambda x, y: x + y, n)
#print(reduce_res)

#4 задание
#def dostavka(s, p):
#    d = 0
#    Kv = ['Al-Farabi','Saina','Tashkentskogo','Dostyk', 'Zhandosova','Tole Bi','Zhubanov', 
# 'Tlendieva','Raymbeka','Rozybakieva','Masanchi','Mukanova']
#    if s in Kv:
#        if p < 10000:
#            d = 500
#        else:
#            d = 0
#    else:
#        if p <= 10000:
#            d = 1000
#        else:
#            d = 1500
#    return d
#
#s = 'Satbayeva'
#p = 19999
#print(dostavka(s, p))

#5 задание
def f1(f, g):
    def h(x):
        return f(g(x))
    return h
def double(x):
    return x*2
def minus(x):
    return x-(x/4)

n = f1(double, minus)
res = n(2000)
print(res)