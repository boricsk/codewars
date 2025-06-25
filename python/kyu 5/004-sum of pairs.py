"""
Adott egy egész számok listája és egyetlen összegérték, adja vissza az első két 
értéket (kérjük, elemezze balról) megjelenési sorrendben, amelyek kiadják 
az összeget.

Ha két vagy több pár van a szükséges összeggel, akkor az a pár a megoldás, 
amelynek második eleme a legkisebb indexű.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * the correct answer is the pair whose second value has the smallest index
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined/Nothing (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * the correct answer is the pair whose second value has the smallest index
== [3, 7]
"""
import numpy as np
test1 = [11, 3, 7, 5]
test2 = [4, 3, 2, 3, 4]
test3 = [0, 0, -2, 3]
test4 = [10, 5, 2, 3, 7, 5]
test5 = [1, -2, 3, 0, -6, 1]
l5 = [10, 5, 2, 3, 7, 5]

def sum_pairs(ints, s):
    position = []
    ret = []
    ints_np =np.array(ints)
    for index, i in enumerate(ints_np):
        for index2, j in enumerate(ints_np):
            # if i >= s or j >= s:
            #     continue  
            if i + j == s:
                  position.append([index, index2])        
            #print(f"i {i} : j {j} ")
    #Mert a position lista sorban töltődik fel, a legkissebb index lesz az első
    if len(position) != 0:
        ret.append(ints_np[position[0][0]])
        ret.append(ints_np[position[0][1]])
    else:
        return None
    
    return ret

def sum_pairs2(ints, s):
    seen = set()
    for num in ints:
        target = s - num
        if target in seen:
            return [target, num]
        seen.add(num)
    return None



print(sum_pairs2(l5 ,10))