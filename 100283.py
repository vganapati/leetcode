from collections import Counter

def minAnagramLength(s):
    def getFactors(k):
        factors_0 = []
        factors_1 = []
        for i in range(1,int(k**0.5)+1):
            if k % i == 0:
                factors_0.append(i)
                if k//i != i:
                    factors_1.insert(0,k//i)
        return factors_0 + factors_1
    
    factors = getFactors(len(s))

    for f in factors:
        anagram = Counter(s[0:f])
        flag = True
        for i in range(1,len(s)//f):
            anagram_i = Counter(s[i*f:(i+1)*f])
            if anagram_i == anagram:
                pass
            else:
                flag = False
                break
        if flag:
            break
    
    return f


def test_0():
    s = "abba"
    assert minAnagramLength(s) == 2

def test_1():
    s = "cdef"
    assert minAnagramLength(s) == 4

def test_2():
    s = "aabb"
    assert minAnagramLength(s) == 4

if __name__ == '__main__':
    test_0()
    test_1()
    test_2()
    


