def sale_hotdogs(n):
    # your code here
    if n < 5: return n * 100
    elif 5 <= n < 10: return n * 95
    else: return n * 90
    
#others
def sale_hotdogs(n):
    return n * (100 if n < 5 else 95 if n < 10 else 90)

def sale_hotdogs(n):
    rate = 100 if n<5 else 95 if n<10 else 90
    return n * rate

def sale_hotdogs(n):
    return n * [90, 95, 100][(n<10) + (n<5)]