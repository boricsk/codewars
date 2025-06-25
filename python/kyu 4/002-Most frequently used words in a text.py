"""
Írjon egy függvényt, amely adott szöveges karakterlánccal (esetleg írásjelekkel és sortörésekkel) 
visszaadja a 3 leggyakrabban előforduló szó tömbjét, az előfordulások számának megfelelő csökkenő sorrendben.

Feltételezések:
A szó egy betűsor (A-tól Z-ig), amely opcionálisan egy vagy több aposztrófot (') tartalmaz az ASCII-ben.
Aposztrófok jelenhetnek meg a szó elején, közepén vagy végén (az „abc, abc”, „abc”, ab'c mind érvényesek)
A többi karakter (pl. #, \, / , . ...) nem része a szónak, és szóközként kell kezelni.
A találatok között nem kell megkülönböztetni a kis- és nagybetűket, és az eredményben szereplő szavakat kisbetűvel kell írni.
A kötelékek önkényesen megszakadhatnak.
Ha egy szöveg háromnál kevesebb egyedi szót tartalmaz, akkor vagy a top-2 vagy a top-1 szavakat kell visszaadni, 
vagy egy üres tömböt, ha a szöveg nem tartalmaz szavakat.

Példák:
"In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."

--> ["a", "of", "on"]


"e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"

--> ["e", "ddd", "aa"]


"  //wont won't won't"

--> ["won't", "wont"]

test.assert_equals(top_3_words("  , e   .. "), ["e"])
test.assert_equals(top_3_words("  ...  "), [])
test.assert_equals(top_3_words("  '  "), [])
test.assert_equals(top_3_words("  '''  "), [])

textf = ''.join(char.lower() if char.isalpha() or char == ' ' or char == "'" else ' ' for char in text).split(' ')

"""

test_text1 = "a a a  b  c c  d d d d  e e e e e"
test_text2 = "  , e   .. "
test_text3 = "  ...  "
test_text4 = "  '''  "


import re
def top_3_words(text):
    ret = []
    count = {}
    input_list2 = []
    input_list = ''.join(char.lower() if char.isalpha() or char == ' ' or char == "'" else ' ' for char in text).split(' ')
   # print(input_list)
    for words in input_list:
        if words != '' and words != "'" and words != "''" and words != "'''":
            input_list2.append(words)
            count.update({words : input_list2.count(words)})            

    sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    
    if len(sorted_count) >= 3:
        sorted_count = dict(list(sorted_count.items())[:3])
    elif len(sorted_count) == 2:
        sorted_count = dict(list(sorted_count.items())[:2])
    elif len(sorted_count) == 1:
        sorted_count = dict(list(sorted_count.items())[:1])
        
    if sorted_count:
        for sorted_items in sorted_count:
            ret.append(sorted_items)
    else:
        ret = []
    
    return ret

def top_3_words2(text):
    ret = []
    count = {}
    input_list2 = []
    input_list = ''.join(char.lower() if char.isalpha() or char == ' ' or char == "'" else ' ' for char in text).split(' ')
    reject_chars = ['', "'", "''", "'''"]
    
    for words in input_list:
        if words not in reject_chars:
            input_list2.append(words)
            count.update({words : input_list2.count(words)})            

    sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    
    if len(sorted_count) >= 3:
        sorted_count = dict(list(sorted_count.items())[:3])
    elif len(sorted_count) == 2:
        sorted_count = dict(list(sorted_count.items())[:2])
    elif len(sorted_count) == 1:
        sorted_count = dict(list(sorted_count.items())[:1])
        
    if sorted_count:
        for sorted_items in sorted_count:
            ret.append(sorted_items)
    else:
        ret = []
    
    return ret

print(top_3_words(test_text1))
print(top_3_words(test_text2))
print(top_3_words(test_text3))
print(top_3_words(test_text4))
