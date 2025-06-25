"""
https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

Rendben, nyomozó, az egyik kollégánk sikeresen megfigyelte célszemélyünket, 
Robbyt, a rablót. Követtük őt egy titkos raktárba, ahol feltételezzük, hogy 
megtaláljuk az összes ellopott holmit. Ennek a raktárnak az ajtaját elektronikus 
kombinációs zár biztosítja. Sajnos a kémünk nem biztos a PIN-kódban, amit látott, 
amikor Robby beírta.
A billentyűzet a következő elrendezéssel rendelkezik:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘

Feljegyezte a 1357-es PIN kódot, de azt is elmondta, lehetséges, hogy az általa 
látott számjegyek mindegyike valójában egy másik szomszédos számjegy (vízszintesen 
vagy függőlegesen, de nem átlósan). Például. az 1 helyett a 2 vagy a 4 is lehet. 
És az 5 helyett a 2, 4, 6 vagy 8 is lehet.

Említette azt is, ismeri ezt a fajta zárat. Korlátlan mennyiségű rossz PIN kódot 
adhat meg, ezek soha nem zárják le a rendszert, és soha nem riasztanak. 
Ezért minden lehetséges (*) variációt kipróbálhatunk.

* lehetséges a következő értelemben: maga a megfigyelt PIN és minden variáció, 
figyelembe véve a szomszédos számjegyeket

Segítene nekünk megtalálni ezeket a változatokat? Jó lenne, ha lenne egy 
függvény, amely egy tömböt (vagy Java/Kotlin és C# nyelven egy listát) ad vissza 
egy megfigyelt PIN kód összes változatának 1-8 számjegy hosszúságú változatait. 
A függvényt getPIN-nek nevezhetnénk (pythonban get_pins, C#-ban GetPINs). 
De vegye figyelembe, hogy minden PIN-kódnak, a megfigyeltnek és az eredményeknek 
is karakterláncnak kell lennie, az esetlegesen vezető 0-k miatt. Már 
elkészítettünk néhány tesztesetet az Ön számára.

Nyomozó, számítunk rád!
"""

test_cases = [
    ('8', ['5','7','8','9','0']),
    ('11',["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
    ('369', [
        "339","366","399","658","636","258","268","669","668","266","369","398",
        "256","296","259","368","638","396","238","356","659","639","666","359",
        "336","299","338","696","269","358","656","698","699","298","236","239"
    ])
]
import itertools

def get_pins(observed):
    affected_nums = {
        "1" : ["1", "2", "4"],
        "2" : ["1", "2", "3", "5"],
        "3" : ["2", "3", "6"],
        "4" : ["4", "1", "7", "5"],
        "5" : ["5", "2", "4", "6", "8"],
        "6" : ["6", "5", "9", "3"],
        "7" : ["7", "4", "8"],
        "8" : ["8", "5", "7", "9", "0"],
        "9" : ["6", "9", "8"],
        "0" : ["8", "0"]
    } 
    elements = []
    for i in observed:
        elements.append(affected_nums.get(i))
    combinations = list(itertools.product(*elements))
    return [''.join(c) for c in combinations]
    
    
print(get_pins('008'))