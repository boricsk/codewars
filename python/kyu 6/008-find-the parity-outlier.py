'''
Kapunk egy egész számokat tartalmazó tömböt (amelynek legalább 3 hosszúságú lesz, de nagyon nagy is lehet). 
A tömb vagy teljesen páratlan egész számokból áll, vagy teljes egészében páros egész számokból áll, kivéve egyetlen N egész számot. 
Írjon egy metódust, amely a tömböt veszi argumentumként, és ezt a "kiugró" N-t adja vissza.
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
'''

def find_outlier(integers):
    tempEven, tempOdd = [], []
   
    for i in integers:
        if i % 2 == 0:
            tempEven.append(i)
           
        else:
            tempOdd.append(i)
            
    if len(tempOdd) == 1:
        return tempOdd[0]
    else:
        return tempEven[0]

print(find_outlier([1,3,5,7,9,2]))
#print(find_outlier([2,4,6,8,9,2]))

#others
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]