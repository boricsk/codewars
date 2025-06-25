"""
Given the triangle of consecutive odd numbers:
             1                      1
          3     5                   8
       7     9    11                27
   13    15    17    19             64
21    23    25    27    29          125
...

Calculate the sum of the numbers in the nth row of this triangle (starting at 
index 1) e.g.: (Input --> Output)
1 -->  1
2 --> 3 + 5 = 8
"""

def row_sum_odd_numbers(n):
    #your code here
    row_start = ((n * n) - n ) + 1
    sum = 0
    if n <= 3:
        return n ** 3 
    else:
        for i in range(row_start,row_start + 2 * n,2):
            sum += i
    return sum

#Vagy

def row_sum_odd_numbers2(n):
    #your code here
    return n ** 3

def test1(n):
    row_start = ((n * n) - n ) + 1
    sum = 0
    for i in range(row_start,row_start + 2 * n,2):
        sum += i
    return sum

list = [x for x in range(100) if x % 2 !=0]
print(list)

test1(41)