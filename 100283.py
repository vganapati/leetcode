def minAnagramLength(s):
    def getFactors(k):
        factors_0 = []
        factors_1 = []
        for i in range(1,int(k**0.5)):
            if k % i == 0:
                factors_0.append(i)
                if k//i != i:
                    factors_1.insert(0,k//i)
        return factors_0 + factors_1
    factors = getFactors(len(s))

    position = 0
    trial_anagram = {s[0]: 1}
    current_anagram
    while position < len(s):




def minAnagramLength_0(s):
    find_anagram_len = lambda anagram: sum([trial_anagram[i] for i in trial_anagram.keys()])
    trial_anagram = {} # shortest possible anagram
    current_anagram = {} # current collection
    full_anagram = {} # everything so far
    trial_anagram_len = find_anagram_len(trial_anagram)
    
    current_len = 0
    for character in s:
        
        current_len += 1

        try:
            current_anagram[character] += 1
        except KeyError:
            current_anagram[character] = 1

        try:
            full_anagram[character] += 1
        except KeyError:
            full_anagram[character] = 1

        # check if current_anagram is a subset of trial_anagram by checking latest addition
        
        if (character in trial_anagram.keys()) and current_anagram[character] <= trial_anagram[character]:
            pass
        else:
            
            current_anagram = dict(full_anagram)
            trial_anagram = dict(full_anagram)
            trial_anagram_len = find_anagram_len(trial_anagram)
            current_len = trial_anagram_len


        if current_len == trial_anagram_len:
            current_anagram = {}
            current_len = 0
    
    breakpoint()
    return find_anagram_len(trial_anagram)

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
    test_2()
    breakpoint()
    test_0()
    test_1()
    


