"""
A fő ötlet az, hogy megszámoljuk az összes előforduló karaktert egy 
karakterláncban. Ha van egy karakterlánca, például az aba, akkor az 
eredménynek {'a': 2, 'b': 1} kell lennie.

Mi van, ha a karakterlánc üres? Ekkor az eredmény üres objektum literál 
legyen, {}.
"""

test1 = ''
test2 = 'aaabbgfddde'

def count(s):
    ret = {}
    # The function code should be here
    if s == '':
        return {}
    else:
        for i in s:
            if i not in ret:
                ret[i] = 1
            else:
                ret[i] += 1
    return ret

print(count(test2))