'''
Egy középiskolának furcsa igazgatója van. Az első napon tanítványai egy furcsa nyitónapi ünnepséget hajtanak végre:

Az iskolában zárható szekrények száma "n" és tanulólétszáma "n" van. Az igazgató megkéri az első tanulót, hogy menjen minden szekrényhez és nyissa ki. 
Aztán megkéri a második diákot, hogy menjen minden második szekrényhez, és zárja be. A harmadik minden harmadik szekrényhez megy, és ha zárva van, kinyitja, 
ha nyitva van, akkor becsukja. A negyedik diák ezt csinálja minden negyedik szekrénynél, és így tovább. Miután az "n"-edik tanulóval befejeződött a folyamat, 
hány szekrény van nyitva?

A feladat egy függvény írása, amely tetszőleges számot kap bemenetként, és visszaadja a nyitott szekrények számát, miután az utolsó sudent befejezte a tevékenységét. 
Tehát a funkció bevitele csak egy szám, amely a szekrények számát és a tanulók számát mutatja. 
Például, ha 1000 szekrény és 1000 diák van az iskolában, akkor a bemenet értéke 1000, és a függvény a nyitott szekrények számát adja vissza, 
miután az 1000. tanuló befejezte a műveletet.

A megadott bemenet mindig nullánál nagyobb vagy azzal egyenlő egész szám, ezért nincs szükség érvényesítésre.
'''

def num_of_open_lockers(n):
    #your code here
    # count = 0
    # for i in range(1, n + 1):
    #     sqr = i ** 0.5
    #     if sqr == int(sqr):
    #         count += 1
    return len([x for x in range(1,n+1) if x**0.5 == int(x**0.5)])

print(num_of_open_lockers(128))

def num_of_open_lockers(n):
    return int(n**0.5)

