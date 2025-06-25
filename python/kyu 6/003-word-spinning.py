"""
Írjon egy függvényt, amely egy vagy több szóból álló sztringet vesz fel, és ugyanazt a karakterláncot adja vissza, de mind az öt vagy több betűs szót fordítva 
(Ugyanúgy, mint ennek a Kata-nak a neve). Az átadott karakterláncok csak betűkből és szóközökből állnak. A szóközök csak akkor jelennek meg, ha egynél több szó van jelen.

Példák:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"

Testing for sentence = 
'will like more consist only letter a and returns Write five name with with Kata Strings present words Spaces letter words name'
'will like more tsisnoc only rettel a and snruter Write five name with with Kata sgnirtS tneserp words secapS rettel words name' 

should equal 
'will like more tsisnoc only rettel a and snruter etirW five name with with Kata sgnirtS tneserp sdrow secapS rettel sdrow name'

"""

def spin_words(sentence):
    # Your code goes here
    sentenceList = sentence.split()
    output = ''
    wordPos = 1
    for word in sentenceList:
        if len(word) >= 5:
            reverseWord = ''.join(reversed([char for char in word]))
            if wordPos < len(sentenceList):
                output += reverseWord + ' '
            else:
                output += reverseWord
            wordPos += 1
        else:
            if wordPos < len(sentenceList):
                output += word + ' '
            else:
                output += word
            
            wordPos += 1
    return output

print(spin_words('will like more consist only letter a and returns Write five name with with Kata Strings present words Spaces letter words name'))

#others

def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

def spin_words(sentence):
    L = sentence.split()
    new = []
    for word in L:
        if len(word) >= 5:
            new.append(word[::-1])
        else:
            new.append(word)
    string = " ".join(new)
    return string