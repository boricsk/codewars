"""
Given an array of ones and zeroes, convert the equivalent binary value to an integer.
Eg= [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples=
Testing= [0, 0, 0, 1] ==> 1
Testing= [0, 0, 1, 0] ==> 2
Testing= [0, 1, 0, 1] ==> 5
Testing= [1, 0, 0, 1] ==> 9
Testing= [0, 0, 1, 0] ==> 2
Testing= [0, 1, 1, 0] ==> 6
Testing= [1, 1, 1, 1] ==> 15
Testing= [1, 0, 1, 1] ==> 11

"""
Testing1 = [0, 0, 0, 1] 
Testing2 = [0, 0, 1, 0] 
Testing3 = [0, 1, 0, 1] 
Testing4 = [1, 0, 0, 1] 
Testing5 = [0, 0, 1, 0] 
Testing6 = [0, 1, 1, 0] 
Testing7 = [1, 1, 1, 1] 
Testing8 = [1, 0, 1, 1] 

def binary_array_to_number(arr):
    bin = ''
    for i in arr:
        bin += str(i)
    return int(bin, 2)


binary_array_to_number(Testing1)