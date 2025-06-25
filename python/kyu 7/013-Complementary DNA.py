"""
A dezoxiribonukleinsav (DNS) a sejtek magjában található vegyi anyag, amely az 
élő szervezetek fejlődésére és működésére vonatkozó "utasításokat" hordozza.

Ha többet szeretne tudni: http://en.wikipedia.org/wiki/DNA

A DNS-láncokban az „A” és „T” szimbólumok egymás kiegészítései, mint „C” és „G”. 
Az Ön függvénye megkapja a DNS egyik oldalát (karakterlánc, kivéve Haskell); 
vissza kell adnia a másik kiegészítő oldalt. A DNS-szál soha nem üres, vagy 
egyáltalán nincs DNS (ismét, Haskell kivételével).

További hasonló gyakorlatok itt találhatók: 
http://rosalind.info/problems/list-view/ (forrás)

Példa: (bemenet --> kimenet)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"

"""

def DNA_strand(dna):
    dna = dna.upper()
    ret = ''
    for i in dna:
        if i == 'A':
            ret += 'T'
        elif i == 'T':
            ret += 'A'
        elif i == 'c':
            ret += 'G'
        elif i == 'G':
            ret += 'C'
        else:
            ret += i
                    
    return ret

print(DNA_strand('GTAT'))