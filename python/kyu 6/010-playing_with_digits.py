"""
Néhány számnak vicces tulajdonságai vannak. Például:

89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴ = 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
Adott két n és p pozitív egész szám, ha létezik olyan pozitív k egész szám, amelyre a p-ből kiinduló, 
egymást követő hatványokra emelt n számjegyek összege egyenlő k * n-nel.

Más szóval, ha n egymást követő számjegyeit a, b, c, d ...-ként írjuk fel, van-e olyan k egész szám, amelyre:
(a**p + b**p+1 + c**p+2 + d**p+3 +...)=n∗k
"""

def dig_pow(n, p):
    # your code
    digits = []
    res = 0
    n2 = n
    
    while n > 0:
        digits.append(n % 10)
        n //= 10
    digits.reverse()
    
    for nums in digits:
        res += (nums ** p)
        p += 1
    
    if res % n2 == 0:
        return int(res / n2)
    else:
        return(-1)
    
    

dig_pow(46288,3)