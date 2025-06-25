"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.

For example, for [1, 2, 2] it should return 9 because 

"""
def square_sum(numbers):
    res = 0
    for i in numbers:
        res += i ** 2
    return res

print(square_sum([1,2,2]))