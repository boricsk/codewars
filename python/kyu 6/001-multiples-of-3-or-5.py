'''
A feladat:
A kapott szám alatt összeadni minden olyan számot ami 3-al és 5-el osztható, ha a kapott szám negatív 0-val térjen vissza,
ha 3-al és 5-el is osztható csak az egyiket számolja.
'''

def solution(number):
    sum = 0
    if number < 0: return 0
    for i in range(number):
        if i % 3==0 or i % 5 == 0:
            sum +=i
    return sum
    
#Más megoldás:
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)