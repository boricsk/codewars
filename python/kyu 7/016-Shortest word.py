"""
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.

"""
import sys
test1 = "bitcoin take over the world maybe who knows perhaps"
test2 = "turns out random test cases are easier than writing out basic ones"
test3 = "lets talk about javascript the best language"
test4 = "i want to travel the world writing code one day"
test5 = "Lets all go on holiday somewhere very cold"
test6 = "Let's travel abroad shall we"

def find_short(s):
    l = sys.maxsize
    str_arr = s.split()
    for i in str_arr:
        if len(i) < l:
            l = len(i)
    return l # l: shortest word length

print(find_short(test1))