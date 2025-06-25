"""
Ennek a gyakorlatnak az a célja, hogy egy karakterláncot egy új karakterláncgá alakítson át, 
ahol az új karakterlánc minden karaktere "(" ha ez a karakter csak egyszer szerepel az 
eredeti karakterláncban, vagy ")", ha ez a karakter többször szerepel az eredetiben.  
Hagyja figyelmen kívül a nagybetűket, amikor megállapítja, hogy egy karakter ismétlődő-e.

Példák
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
"""
import re
def duplicate_encode(word):
    word = word.lower()
    ret = ''
    for char in word:        
        if word.count(char) > 1:
            ret += ')'
        else:
            ret += '('
    print(ret)

duplicate_encode('(( @')
#Regex csak akkor működik jól, ha nincs spec. karakter a stringben.