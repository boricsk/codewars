"""
Adott két a és b egész szám, amelyek lehetnek pozitívak vagy negatívak, 
keresse meg a közöttük lévő összes egész szám összegét, és adja vissza. 
Ha a két szám egyenlő, akkor adjon vissza a vagy b.

Megjegyzés: a és b nincs sorrendben!

(1, 0) --> 1 (1 + 0 = 1)
(1, 2) --> 3 (1 + 2 = 3)
(0, 1) --> 1 (0 + 1 = 1)
(1, 1) --> 1 (1 since both are same)
(-1, 0) --> -1 (-1 + 0 = -1)
(-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

"""

def get_sum(a,b):
    if a > b:
        a,b = b,a
    return sum([x for x in range(a,b+1)])

print(get_sum(-2,10))