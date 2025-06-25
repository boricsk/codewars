# https://www.codewars.com/kata/54da539698b8a2ad76000228
"""
Kezdőérték definiálás (x, y) == (0, 0).
a. Ha az utasítás 'n', növeld az y értéket.
b. Ha az utasítás 's', csökkentsd az y értéket.
c. Ha az utasítás 'e', növeld az x értéket.
d. Ha az utasítás 'w', csökkentsd az x értéket.
"""
test1 = ['n','s','n','s','n','s','n','s','n','s'] #T
test2 = ['w','e','w','e','w','e','w','e','w','e','w','e'] #F
test3 = ['n','n','n','s','n','s','n','s','n','s'] #F (Nem ugyanoda ér vissza)
failwalk = [ ['n'], ['n','s'], ['n','s','n','s','n','s','n','s','n','s','n','s'], ['n','s','e','w','n','s','e','w','n','s','e','w','n','s','e','w'], ['n','s','n','s','n','s','n','s','n','n'], ['e','e','e','w','n','s','n','s','e','w'], ['n','s','e','w','n','s','e','w','n','s','e','w','n','s','e','w','n','s','e','w'], ['s','s','s','s','s','w','w','n'] ]


def is_valid_walk2(walk):
    return (len(walk) == 10) and (walk.count('n') == walk.count('s')) and (walk.count('e') == walk.count('w'))


def is_valid_walk(walk):
    x, y = 0
    if len(walk) == 10: 
        for i in walk:
            if i == 'n':
                y += 1
            elif i == 's':
                y -= 1
            elif i == 'e':
                x += 1
            elif i == 'w':
                x -= 1
    
    return (x == 0) and (y == 0) and (len(walk) == 10)

print(is_valid_walk2(test1))
print(is_valid_walk2(test2))
print(is_valid_walk2(test3))

for items in failwalk:
    print(is_valid_walk2(items))