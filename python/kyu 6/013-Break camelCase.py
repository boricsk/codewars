"""
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""

def solution(s):
    ret = ''
    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 90:
            ret += ' '+ s[i]
        else:
            ret += s[i] 
    return ret

print(solution('camelCasing'))