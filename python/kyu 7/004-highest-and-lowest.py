#a kapott szóközzel elválasztott számok közül a legkisebbel és legnagyobbal kell visszatérni
"""
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"

"""
def high_and_low(numbers):
    # ...
    numberList = numbers.split()
    numberListInt = [eval(i) for i in numberList]
    returnValue = str(max(numberListInt)) + ' ' + str(min(numberListInt))
    return returnValue

high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")

#others
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))

def high_and_low(numbers):
    nums = sorted(numbers.split(), key=int)
    return '{} {}'.format(nums[-1], nums[0])

def high_and_low(numbers):
  return " ".join(x(numbers.split(), key=int) for x in (max, min))