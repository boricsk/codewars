#Fordísd meg a szavakat a kapott mondatban
#https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
test1 = 'The quick brown fox jumps over the lazy dog.'
test2 = 'apple'
test3 = 'a b c d'
test4 = 'double  spaced  words'
test5 = " elbuod  decaps  sdrow" # should equal 'elbuod  decaps  sdrow'"

def reverse_words(text):
    # Felosztjuk a szöveget szóközök alapján, így megkapjuk a szavakat és a szóközök megtartásával.
    words = text.split(' ')
    print(words)
    # Létrehozunk egy listát, amelybe a megfordított szavakat fogjuk tárolni.
    reversed_words = []
    
    # Végigmegyünk minden szón a listában.
    for word in words:
        # Megfordítjuk az aktuális szót és hozzáadjuk a listához.
        reversed_words.append(word[::-1])
    print(reverse_words)
    # A megfordított szavakat visszaalakítjuk egy sztringgé, ahol a szóközök megmaradnak.
    return ' '.join(reversed_words)

def reverse_words2(text):
    return ' '.join(word[::-1] for word in text.split(' '))

print(reverse_words(test5))