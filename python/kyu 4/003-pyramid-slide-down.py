'''
Dalszöveg...

A piramisok csodálatosak! Mind építészeti, mind matematikai értelemben. Ha van számítógéped, akkor is vacakolhatsz piramisokkal, ha éppen nem Egyiptomban vagy. 
Vegyük például a következő problémát. Képzeld el, hogy van egy számokból felépített piramisod, mint például itt:

/3/
\7\ 4
2 \4\ 6
8 5 \9\ 3

Itt jön a feladat...

Tegyük fel, hogy a „lecsúszás” a piramis tetejétől az aljáig egymást követő számok maximális összege. Amint látja, a leghosszabb 'lecsúszás' 3 + 7 + 4 + 9 = 23

Az Ön feladata, hogy írjon egy függvényt, amely egy piramisábrázolást vesz argumentumnak, és visszaadja a „legnagyobb lecsúszását”. Például:

* A `[[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]] bemenettel
* A függvénynek a "23" értéket kell visszaadnia.

Apropó...

A tesztjeim között szerepel néhány rendkívül magas piramis is, így ahogy sejtheti, a brute force módszer rossz ötlet, hacsak nincs vesztegetni való néhány évszázad. 
Valami okosabbat kell kitalálnod ennél.

(c) Ez a feladat a ProjectEuler 18. és/vagy 67. feladatának szöveges változata.
Algoritmusok
Dinamikus programozás

[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20,  4, 82, 47, 65],
[19,  1, 23, 75,  3, 34],
[88,  2, 77, 73,  7, 63, 67],
[99, 65,  4, 28,  6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]), 1074)
'''

def longest_slide_down(pyramid):
    #print(len(pyramid))
    result, currentIndex, currentValue, outherIteration = 0, 0, 0, 0
    for items in pyramid:
        print(max(items))
        if len(items) == 1 or len(items) == 2:
            result += max(items)
            currentIndex = items.index(max(items))
            currentValue = max(items)
            print('current index', currentIndex)
        elif outherIteration > 2:
            for i in range(len(items)):
                if i-currentIndex == 0:
                    if items[i] > currentValue:
                        result += items[i]
                        currentIndex = i
                        currentValue = items[i]
                    elif items[i+1] > currentValue:
                        result += items[i+1]
                        currentIndex = i+1
                        currentValue = items[i+1]
                    
        
        outherIteration += 1
        print('Out iter', outherIteration)
    
    return result

print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))