"""
egy számról meg kell mondani, hogy páros vagy páratlan
"""

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

#Other 
def even_or_odd(number):
    return ["Even", "Odd"][number % 2]
