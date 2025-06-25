"""
A Western Suburbs Croquet Clubnak két tagsági kategóriája van: Senior és Open. 
Segítséget szeretnének kérni egy jelentkezési laphoz, amelyen a leendő tagok 
megtudhatják, melyik kategóriába kerülnek.

Ahhoz, hogy egy tag senior legyen , legalább 55 évesnek kell lennie, és 7-nél 
nagyobb fogyatékossággal kell rendelkeznie. Ebben a krokett klubban a 
fogyatékosság -2 és +26 között van; minél jobb a játékos, annál kisebb a hendikep.
Bemenet

A bemenet a párok listájából fog állni. Mindegyik pár egyetlen lehetséges tagra 
vonatkozó információt tartalmaz. Az információ egy egész számból áll a személy 
életkorára és egy egész számból a személy fogyatékosságára vonatkozóan.
Kimenet

A kimenet egy karakterlánc-értékek listájából fog állni (Haskell és C nyelven: 
Open vagy Senior), amely jelzi, hogy az adott tagot senior vagy nyílt 
kategóriába kell-e helyezni.

input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
"""

input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
input2 = [(18, 2), (31, 0), (38, 5), (62, 7), (36, 19), (11, 14), (53, 7), (85, 6)]

def open_or_senior(data):
    ret = []
    return ['Senior' if i[0] >=55 and i[1] > 7 else 'Open' for i in data]

print(open_or_senior(input2))