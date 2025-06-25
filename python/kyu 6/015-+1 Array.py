"""
Adott egy tetszőleges hosszúságú egész számokból álló tömböt, adjon vissza egy 
olyan tömböt, amely 1-gyel egészíti ki a tömb által képviselt értéket.

Ha a tömb érvénytelen (üres vagy negatív egész számokat vagy 1 számjegynél több 
egész számokat tartalmaz), adjon nullát (vagy az Ön nyelvének megfelelőjét).


    [4, 3, 2, 5] would return [4, 3, 2, 6] (4325 + 1 = 4326)
    [1, 2, 3, 9] would return [1, 2, 4, 0] (1239 + 1 = 1240)
    [9, 9, 9, 9] would return [1, 0, 0, 0, 0] (9999 + 1 = 10000)
    [0, 1, 3, 7] would return [0, 1, 3, 8] (0137 + 1 = 0138)

Invalid arrays

    [] is invalid because it is empty
    [1, -9] is invalid because -9 is not a non-negative integer
    [1, 2, 33] is invalid because 33 is not a single-digit integer

"""
t1 = [1, 1, 3, 7]
t2 = [0]

arr1=[0, 0, 5, 7, 4, 2, 4, 8, 8, 6, 6, 8, 2, 9, 2, 6, 0, 6, 7, 5, 1]
#   [0, 5, 7, 4, 2, 4, 8, 8, 6, 6, 8, 2, 9, 2, 6, 0, 6, 7, 5, 2] 
# should equal [0, 0, 5, 7, 4, 2, 4, 8, 8, 6, 6, 8, 2, 9, 2, 6, 0, 6, 7, 5, 2]

def up_array(arr):
    arr_int = 0
    valid_numbers = [0,1,2,3,4,5,6,7,8,9]
    ret = []
    
    if (arr == []):
        return None
    
    if (arr == [0]):
        return [1]
    
    for num in arr:
        if (num not in valid_numbers):
            #is_num_ok = False
            return None

    arr_int = int(''.join(str(i) for i in arr)) + 1
    
    for k in arr:
        if (k == 0):
            ret.append(0)
        elif (k != 0):
            break
        
    for j in str(arr_int):
            ret.append(int(j))
    #ret = [int(num) for num in str(arr_int)]

    return ret

print(up_array(arr1))