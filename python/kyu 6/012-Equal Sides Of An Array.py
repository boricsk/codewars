"""
Egész számokból álló tömböt fog kapni. Az Ön feladata, hogy vegye ezt a tömböt, 
és keressen egy N indexet, ahol az N-től balra lévő egész számok összege egyenlő 
az N-től jobbra lévő egész számok összegével.

Ha nincs olyan index, amely ezt megvalósítaná, adja vissza a -1-et.
Például:

Tegyük fel, hogy megkapta az {1,2,3,4,3,2,1} tömböt:
A függvény a 3-as indexet adja vissza, mivel a tömb 3. pozíciójában az index bal 
oldalának összege ({1,2,3}) és az index jobb oldalának összege ({3,2, 1}) 
mindkettő egyenlő 6.

Nézzünk egy másikat.
A következő tömböt kapja: {1,100,50,-51,1,1}:
A függvény az 1-es indexet adja vissza, mivel a tömb 1. pozíciójában az index 
bal oldalának összege ({1}) és az index jobb oldalának összege ({50,-51,1,1) }) 
mindkettő egyenlő 1-gyel.

Utolsó:
A következő tömböt kapja: {20,10,-80,10,10,15,35}
A 0 indexnél a bal oldal {}
A jobb oldal {10,-80,10,10,15,35}
Összeadáskor mindkettő egyenlő 0-val. (Ebben a feladatban az üres tömbök 0-val 
egyenlőek)
A 0 index az a hely, ahol a bal és a jobb oldal egyenlő.

Megjegyzés: Ne feledje, hogy a legtöbb nyelven egy tömb indexe 0-val kezdődik.

       [1,2,3,4,3,2,1]),3)
       [1,100,50,-51,1,1]),1,)
       [1,2,3,4,5,6]),-1)
       [20,10,30,10,10,15,35]),3)
       [20,10,-80,10,10,15,35]),0)
       [10,-80,10,10,15,35,20]),6)
       list(range(1,100))),-1)
       [0,0,0,0,0]),0,"Should pick the first index if more cases are valid")
       [-1,-2,-3,-4,-3,-2,-1]),3)
       list(range(-100,-1))),-1)
       [8,8]),-1)
       [8,0]),0)
       [0,8]),1)
       [7,3,-3]),0)
       [8]),0)
       [10,-10]),-1)
       [-3,2,1,0]),3)
       [-15,5,11,17,19,-17,20,-6,17,-17,19,16,-15,-6,20,17]),8)
"""
test1 = [1,2,3,4,3,2,1]
test2 = [1,100,50,-51,1,1]
test3 = [20,10,-80,10,10,15,35]
test4 = [1,2,3,4,3,2,1]
test5 = [1,100,50,-51,1,1]
test6 = [1,2,3,4,5,6]
test7 = [20,10,30,10,10,15,35]
test8 = [20,10,-80,10,10,15,35]
test9 = [10,-80,10,10,15,35,20]
test10 = [0,0,0,0,0]
test11 = [-1,-2,-3,-4,-3,-2,-1]
test12 = [8,8]
test13 = [8,0]
test14 = [0,8]
test15 = [7,3,-3]
test16 = [8]
test17 = [10,-10]
test18 = [-3,2,1,0]
test19 = [-15,5,11,17,19,-17,20,-6,17,-17,19,16,-15,-6,20,17]


def find_even_index(arr):
    ret = 0
    found = False
    for i in range(len(arr)):
        if sum(arr[:(i)]) == sum(arr[(i + 1 ):]):
            ret = i
            found = True
            break
    return ret if found else -1

print(find_even_index(test1))
print(find_even_index(test2))
print(find_even_index(test3))
print(find_even_index(test4))
print(find_even_index(test5))
print(find_even_index(test6))
print(find_even_index(test7))
print(find_even_index(test8))
print(find_even_index(test9))
print(find_even_index(test10))
print(find_even_index(test11))
print(find_even_index(test12))
print(find_even_index(test13))
print(find_even_index(test14))
print(find_even_index(test15))
print(find_even_index(test16))
print(find_even_index(test17))
print(find_even_index(test18))


