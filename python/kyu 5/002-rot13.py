#https://www.codewars.com/kata/530e15517bc88ac656000716/train/python
#ROT13

def rot13(message):
    charTransfer = 13
    codedString = ''
    def isCapital(character):
        return True if 65 < ord(character) < 90 else False

    for char in message:
        if 78 <= ord(char) <= 90:
            codedString += chr(64 + (charTransfer - (90 - ord(char))))
        
        elif 110 <= ord(char) <= 122:
            codedString += chr(96 + (charTransfer - (122 - ord(char))))
        
        elif (97 <= ord(char) <= 97 + charTransfer) or (65 <= ord(char) <= 65 + charTransfer):
            codedString += chr(ord(char) + charTransfer)
        else:
            codedString += char
        
    return codedString

print(rot13('Test'))

#others
import string
from codecs import encode as _dont_use_this_

def rot13(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outputMessage = ""
    for letter in message:
        if letter in alpha.lower():
            outputMessage += alpha[(alpha.lower().index(letter) +13) % 26].lower()
        elif letter in alpha:
            outputMessage += alpha[(alpha.index(letter) +13) % 26]
        else:
            outputMessage += letter
    return outputMessage
    
def rot13(message):
    return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz','NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))

import string

def rot13(message):
    return ''.join(chr((65 if c.isupper() else 97) + ((ord(c) - (65 if c.isupper() else 97)) + 13)%26) if c.isalpha() else c for c in message)