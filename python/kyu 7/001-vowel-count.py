'''
Feladat
Számoljuk meg a magánhangzókat [a, e, i, o, u] egy mondatban. Az input csak kisbetűket és szóközöket tartalmaz.
'''
def get_count(sentence):
    return len([character for character in sentence if character in 'aeiou'])

#Más megoldás
import re
def getCount(str):
    return len(re.findall('[aeiou]', str, re.IGNORECASE)) #IGNORECASE nem tesz különbséget a kis és nagybetűk között. a regex segítségével gyárt egy listát, és ennek a hosszát adja vissza

#végigmegy a megadott listán és a .count -al megszámolja a char, tartalmát (ami a listából jön) és összegezi ezeket.
def getCount(inputStr):
    return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])

#True-false értékeket ad vissza a listának, és ezt összegzi
def getCount(string):
    return sum([i in list('euioa') for i in string])