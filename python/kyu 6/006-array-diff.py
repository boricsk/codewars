'''
A cél ebben a katában egy különbségfüggvény megvalósítása, amely kivonja az egyik listát a másikból, és visszaadja az eredményt.
El kell távolítania az a listából az összes olyan értéket, amely a b listában szerepel, megtartva sorrendjüket.
array_diff([1,2],[1]) == [2]
Ha egy érték jelen van b-ben, akkor minden előfordulását el kell távolítani a másikból:
array_diff([1,2,2,2,3],[2]) == [1,3]
'''
def array_diff(a, b):
    return [x for x in a if x not in b]

print(array_diff([1,2,2,3,2,2],[1,2,9]))