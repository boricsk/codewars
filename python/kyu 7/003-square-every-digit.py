"""
Üdvözöljük. Ebben a katában egy szám minden számjegyét négyzetre kell emelni, és összefűzni őket.

Például, ha a 9119-et futtatjuk a függvényen, akkor a 811181 jön ki, mert a 9^2 az 81, a 1^2 pedig az 1.

Megjegyzés: A függvény egész számot fogad el, és egész számot ad vissza
"""

def square_digits(num):
    str_num = str(num)
    out = ''
    for digit in str_num:
        out += str(int(digit)*int(digit))
    return int(out)
print(square_digits(123))

#orhers
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))