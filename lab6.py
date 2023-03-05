'''
t = ("Alisher","Mansurov","Comp Sciense","3 kurs")
print(t[0:2])  
print(t.count("Alisher"))  
s = {"Alisher","Mansurov","Comp Sciense",3}
s.add("kurs")
print(s)
s.remove("kurs")
print(s)
s.pop()
print(s)
'''
'''
import random
temp = 0
tl = []
for i in range(0,10):
    temp = random.randint(0,5)
    tl.append(temp)
t1 = tuple(tl)
for i in range(0,10):
    temp = random.randint(-5,0)
    tl.append(temp)
t2 = tuple(tl)
res = tuple(t1+t2)
print(res)
print(res.count(0))

t1 = (random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5))
t2 = (random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5),random.randint(0,5))
'''

'''
t = (3,(3.1,(3 + 2j, ("3 и 3", ()))))
print(t[1][1][0])
'''
'''
Res = 0
L = [[780,420,300],[1280,720,900],[780,420,320],[1280,420,380],[780,720,1000],[1280,420,800],[780,720,500]]
for i in range(len(L)):
    for j in range(len(L[i])):
        Res += L[i][j]
print(Res)
'''
'''
res = []
T = tuple(input().lower().split())
for i in T:
    if "ва" in i:
        res.append(i)
print(*res)
'''

Kaz_latin = {
    "А": "A", "Ә": "A'", 
    "Б": "B", "В": "V", 
    "Г": "G", "Ғ": "G'", 
    "Д": "D","Е": "E", 
    "Ё": "E'", "Ж": "J", 
    "З": "Z", "И": "I", 
    "Й": "I'", "К": "K",
    "Қ": "Q", "Л": "L", 
    "М": "M", "Н": "N", 
    "Ң": "N'", "О": "O", 
    "Ө": "O'","П": "P", 
    "Р": "R", "С": "S", 
    "Т": "T", "У": "U", 
    "Ұ": "U'", "Ү": "U'",
    "Ф": "F", "Х": "H", 
    "Һ": "H'", "Ц": "C", 
    "Ч": "Ch", "Ш": "Sh", 
    "Щ": "Sh'","Ъ": "", 
    "Ы": "Y", "І": "I", 
    "Ь": "", "Э": "E", 
    "Ю": "Yu", "Я": "Ya"
}


text = ("Сәлем! Күндеріңіз сәтті өтсін")
text = text.upper()
l = ""

for char in text:
    if char.upper() in Kaz_latin:
        l += Kaz_latin[char.upper()]
    else:
        l += char
l = l.lower()
print("latin: ", l.capitalize())


