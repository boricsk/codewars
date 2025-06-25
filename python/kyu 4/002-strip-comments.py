#CAN NOT SOLVE
'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. 
Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:

apples, pears
grapes
bananas

The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

1. Remove spaces from end of words
apples, pears # and bananas\ngrapes\nbananas !apples

'''
import re
def strip_comments(strng, markers):
    outStr, outStr2 = '', ''
    mustRemove = False
    counter = 0
    for char in strng:
        if char != ' ':
            outStr += char
    
    for char in outStr:
        
        if char in markers:
            mustRemove = True
            if counter != len(outStr):
                outStr2 += '\n'
        else:
            if not mustRemove:
                if char == ',': 
                    outStr2 += char + ' '
                else:
                    outStr2 += char
        if char == '\n':
            #outStr2 += '\n'
            mustRemove = False
        
        counter +=1
        # if mustRemove and char != '\n':
        #     pass
        # else:
        #     mustRemove = False
        
    return repr(outStr2)

# import re
# def strip_comments(strng, markers):
#     regexMarkers = ''.join(char for char in markers)
#     return re.sub(r"(\t*#[a-z\s]*|!.*){1,}|(\t*#[a-z\s]*|!.*)",'', strng)

#re.sub(r'\s*#[a-zA-Z\s]*|!.*$','', strng, flags = re.IGNORECASE)
#re.findall(r'\s*#[a-zA-Z\s]*|!.*$',strng)
#re.search(r'\s*#[a-zA-Z\s]*|!.*$',strng).group(0)
#re.match(r'\s*#[a-zA-Z\s]*|!.*$', strng)
#re.sub(r"(\s*#[a-z\s]*|!.*)|(\s*#[a-z\s]*|!.*)",'', strng, flags = re.IGNORECASE)


print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples',['#', '$', '!']))