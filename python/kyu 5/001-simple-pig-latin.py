'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

'''

def pig_it(text):
    inputList, outputList, punctuation = [], [], ['.',',','?','!','-','+','"','\'',':',';']
    inputList = text.split()
    for i in inputList:
        if i not in punctuation:
            temp = i + i[0]
            outputList.append(temp[1::] + 'ay')
        else:
            temp = i + i[0]
            outputList.append(i)
    
    return ' '.join(outputList)

print(pig_it('Hello o világ !'))

#others
def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

def pig_it(text):
    return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())

import re

def pig_it(text):
    return re.sub(r'([a-z])([a-z]*)', r'\2\1ay', text, flags=re.I)

from string import punctuation
def pig_it(text):
    words = text.split(' ')
    return ' '.join(
        [
            '{}{}ay'.format(
                word[1:],
                word[0]
            ) if word not in punctuation else word for word in words
        ]
    )