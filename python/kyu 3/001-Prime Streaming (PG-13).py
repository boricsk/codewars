"""
Create an endless generator that yields prime numbers. 
The generator must be able to produce a million primes in a few seconds
"""
import datetime
import math
import numpy as np
def stream():
    limit = 60_000_000
    primes = [True] * (limit + 1)  
    p = 2
    while (p * p <= limit):
        if primes[p] == True:  
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
    
    prime_numbers = [p for p in range(2, limit + 1) if primes[p]]
    return prime_numbers


def stream2():
    limit = 15_485_865
    primes = [True] * (limit + 1)  
    p = 2
    while (p * p <= limit):
        if primes[p] == True:  
            for i in range(p * p, limit + 1, p):
                primes[i] = False
        p += 1
        
    prime_numbers = [p for p in range(2, limit + 1) if primes[p]]
    for i in range(len(prime_numbers)):
        yield prime_numbers[i]
    

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



def stream():
    limit = 15_485_865  
    primes = [True] * limit
    primes[0], primes[1] = False, False  

    for base in range(2, int(limit ** 0.5) + 1):
        if primes[base]:
            for multiple in range(base*base, limit, base):
                primes[multiple] = False

    for num in range(2, limit):
        if primes[num]:
            yield num

def stream3():
    limit = 100 #15_485_865  
    primes = [True] * limit
    primes[0] = False 
    primes[1] = False
    
    #Kettővel és hárommal oszthatók kizárása
    for i in range(4, limit):
        if (i % 2 == 0) or (i % 3 == 0):
            primes[i] = False

    for i in range(len(primes)):
        if primes[i] == True:
            print(i)

def sieve_of_eratosthenes(limit):
    sieve = np.array([True] * (limit + 1))
    sieve[0] = sieve[1] = False  
    for start in range(2, int(math.sqrt(limit)) + 1):
        if sieve[start]:
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False
    
    return np.array([num for num, is_prime in enumerate(sieve) if is_prime])

#Ez a verzió lefut 12 másodperc alatt a szerveren, ezt fogadta el.
def stream5():
    limit = 15490000
    # Numpy tömb inicializálása a listák helyett
    primes = np.ones(limit, dtype=bool)  # Minden elem True kezdetben
    primes[:2] = False  # A 0 és 1 nem prím

    # Szitálás a prímszámok kiszűrésére
    for base in range(2, int(limit**0.5) + 1):
        if primes[base]:
            primes[base*2::base] = False  # Az összes többszöröst False-ra állítjuk

    # Generátor az eredményekhez
    p = (num for num in np.nonzero(primes)[0])
    for i in p:
        yield i


    
start = datetime.datetime.now()
# c = 1
# num = 0
# while c <= 1000000:
#     if is_prime(num):
#         c += 1
#     num += 1

# print(num)


stream5()
#print(len(sieve_of_eratosthenes(15_485_865)))
print(f"Execution time : {datetime.datetime.now() - start}")