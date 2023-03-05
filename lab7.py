
#Первое задание
#d = {'kurs':3,'age':20,'dis':7}
#print(d.items())
#print(d.keys())
#d1 = {'kurs':4}
#d.update(d1)
#print(d)
#print(d.values())
#d.clear()
#print(d)

#Второе
#N = 6
#d = {'Irtysh':'Kazakhstan', 'Ili': 'Kazakhstan', 
#     'Volga':'Russia', 'Yenisei':'Russia'}
#r = ['Irtysh','Ili','Volga','Yenisei']
#for i in r:
#    print(i,", ",d[i])
#
#t = input("Enter river: ")
#print(t in d)
#
#d['Ural']='Kazakhstan'
#print(d)

#Третье
#r = {}
#tn = 'a'
#tc = 'a'
#while True:
#    try:
#        tn, tc = map(str, input().split())
#    except ValueError:
#        break
#    else:
#        r[tn]=tc
#print(r)
#print(len(r))

#Четвертое
#l = ['5', 'A 8771 B 8772 C 8773 D 8774 F 8775', 'A']
#r = l[1].split()
#t = 0
#for i in range(len(r)):
#    if l[2] == r[i]:
#        print(r[i+1])
#        t = 1 
#if t == 0:
#    print("Not in the phone book")
#

#Пятый
l = [5, 'A 10 January', 'B 10 February', 'C 10 January', 'D 10 March', 'F 10 April', 'January']
res = []
for i in range(1, l[0]-1):
    t = l[i].split()
    if l[-1] == t[2]:
        res.append(t[0])
r = " ".join(res)
print(r)