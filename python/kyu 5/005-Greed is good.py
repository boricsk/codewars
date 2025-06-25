'''
A kapzsiság egy kockajáték, amelyet öt hatoldalú kockával játszanak. A küldetésed, 
ha úgy döntesz, hogy elfogadod, az, hogy dobj a szabályok szerint. 
Mindig kapsz egy tömböt öt hatoldalú kockaértékkel.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
 
Egy dobókockát csak egyszer lehet megszámolni minden dobásban. Például egy 
adott „5” csak egy hármas részének számíthat (hozzájárulva az 500 ponthoz) 
vagy egyetlen 50 pontnak, de nem mindkettő ugyanabban a dobásban.

Példa

Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

'''
import collections as co
t1 = [5, 1, 3, 4, 1]# ),  250)
t2 = [1, 1, 1, 3, 1]# ), 1100)
t3 = [2, 3, 4, 6, 2]# ),    0)
t4 = [4, 4, 4, 3, 3]# ),  400)
t5 = [2, 4, 4, 5, 4]# ),  450)
t6 = [1, 1, 1, 1, 1]
t7 = [1, 2, 3, 2, 2]#300
t8 = [1, 5, 5, 5, 4]#600
t9 = [5, 2, 1, 1, 1]#1050

def score(dice):
    ret = 0
    stat = co.Counter(dice)
    for key, value in stat.items():
        if key == 1:
            if value >= 3:
                ret += 1000 + (value - 3) * 100
            else:
                ret += value * 100
        elif key == 5:
            if value >= 3:
                ret += key * 100 + (value - 3) * 50
            else:
                ret += value * 50
        else:
            if value == 3:
                ret += key * 100
    return ret

print(score(t8))