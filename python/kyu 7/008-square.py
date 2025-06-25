'''
Négyzet négyzet

Szereted az építőkockákat. Különösen szereted a négyzet alakú építőkockákat. És amit még jobban szeretsz, az az, hogy négyzet alakú építőkockákból rendezd el őket!

Néha azonban nem lehet őket négyzetbe rendezni. Ehelyett egy közönséges téglalapot kapsz! Azok az elrontott dolgok! 
Ha csak módodban áll megtudni, hogy jelenleg hiába dolgozik-e… Várj! Ez az! Csak azt kell ellenőriznie, hogy az építőkockák száma tökéletes-e.
Feladat

Adott egy integrálszám, határozza meg, hogy négyzetszám-e:

     A matematikában a négyzetszám vagy tökéletes négyzet olyan egész szám, amely egy egész szám négyzete; más szóval, valamilyen egész szám szorzata önmagával.

A tesztek mindig valamilyen integrálszámot használnak, ezért ne aggódjon emiatt a dinamikus gépelt nyelveken.
'''
import math
def is_square(n):    
    if n < 0:
        return False
    elif n == 0:
        return True
    if math.sqrt(n) % 1 == 0:
        return True
    else:
        return False

is_square(26)

#others
import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0

import math
def is_square(n):    
    try:
        return math.sqrt(n).is_integer()
    except ValueError:
        return False

def is_square(n):    
    if n>=0:
        if int(n**.5)**2 == n:
            return True
    return False