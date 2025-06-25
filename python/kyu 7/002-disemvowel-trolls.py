'''
Feladat
Trollok támadják a komment rovatodat!

A helyzet kezelésének általános módja az, hogy eltávolítják az összes magánhangzót a trollok megjegyzéseiből, így semlegesítve a fenyegetést.

Az Ön feladata, hogy írjon egy függvényt, amely egy karakterláncot vesz fel, és egy új karakterláncot ad vissza az összes magánhangzó eltávolításával.

Például a "Ez a webhely a veszteseknek készült LOL!" „Ths wbst s fr lsrs LL!” lesz.

Megjegyzés: ehhez a kata y-t nem tekintjük magánhangzónak.

'''

def disemvowel(string_):
    return string_.replace('a', '').replace('e', '').replace('u', '').replace('o', '').replace('i', '').replace('A', '').replace('E', '').replace('U', '').replace('O', '').replace('I', '')

def disemvowel(string_):
    return ''.join([char for char in string_ if char not in 'aeiouAEIOU'])

#others
import re
def disemvowel(string):
    return re.sub('[aeiou]', '', string, flags = re.IGNORECASE)