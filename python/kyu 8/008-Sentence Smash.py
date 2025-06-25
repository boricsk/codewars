
test1 = ["hello"]
test2 = ["hello", "world"]
test3 = ["hello", "amazing", "world"]
test4 = ["this", "is", "a", "really", "long", "sentence"]

def smash(words):
    ret = ''
    for w in words:
        ret += str(w) + ' '
    return ret.strip()

print(smash(test4))

