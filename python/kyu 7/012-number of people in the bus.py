"""
A városban közlekedik egy busz, amely minden buszmegállóba felvesz és lerak 
néhány embert.
Megkapja az egész számpárok listáját (vagy tömbjét). Az egyes párok elemei a 
buszra felszállók számát (első elem) és a buszról leszállók számát (a második elem) 
jelentik egy buszmegállóban.

Az Ön feladata, hogy visszaadja azoknak a számát, akik az utolsó buszmegálló 
után (az utolsó tömb után) még a buszon vannak. Annak ellenére, hogy ez az utolsó 
buszmegálló, lehet, hogy nem üres a busz, és néhány ember még bent van, 
valószínűleg ott alszanak :D

Vessen egy pillantást a tesztesetekre.
Ne feledje, hogy a tesztesetek biztosítják, hogy a buszon tartózkodók száma 
mindig >= 0 legyen. Tehát a visszaadott egész szám nem lehet negatív.
A tömb első párjának második értéke 0, mivel a busz üres az első buszmegállóban.

"""
test1 = [[10,0],[3,5],[5,8]]
test2 = [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]
test3 = [[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]


def number(bus_stops):
    return sum(i[0]-i[1] for i in bus_stops)


print(number(test3))