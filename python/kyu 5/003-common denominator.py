#convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]
import math
def convert_fracts(lst):
    denoms = []
    numers = []
    ret = []
   
    numers = [i[0] for i in lst]
    denoms = [i[1] for i in lst]

    lcm = math.lcm(*denoms)
    
    for i in range(len(numers)):
        numers[i] *= int(lcm / denoms[i])
        ret.append([numers[i], lcm])
    
    return (ret)

test1 = [[1, 2], [1, 3], [1, 4]]

print(convert_fracts(test1))