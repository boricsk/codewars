'''
In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. 
This means, you have to shuffle all letters from the input in all possible orders.

Examples:

* With input 'a'
* Your function should return: ['a']
* With input 'ab'
* Your function should return ['ab', 'ba']
* With input 'aabb'
* Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

'''
from itertools import permutations as perm

def permutations2(s):
    outputListTemp, outputList = [], []
    for p in perm(s):
        if p not in outputListTemp:
            outputListTemp.append(p)
    print(outputListTemp)
    for x in outputListTemp:
        TempStr = ''
        for i in range(len(x)):
            TempStr += x[i]
            
        outputList.append(TempStr)
 
    return outputList

#others
def permutations(s):
    return list(set(''.join(x) for x in perm(s)))

#https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python

print(permutations('aabb'))

def permutations5(string):
  if len(string) == 1: return set(string)
  first = string[0]
  rest = permutations(string[1:])
  result = set()
  for i in range(0, len(string)):
    for p in rest:
      result.add(p[0:i] + first + p[i:])
  return result

from itertools import permutations as perm
out = [''.join(p) for p in perm('abc')]
print(out)