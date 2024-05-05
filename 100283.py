def minAnagramLength(s):
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
            current_anagram = {}
            trial_anagram = dict(full_anagram)
            trial_anagram_len = find_anagram_len(trial_anagram)


        if current_len == trial_anagram_len:
            current_anagram = {}
            current_len = 0

    return find_anagram_len(trial_anagram)

def test_0():
    s = "abba"
    assert minAnagramLength(s) == 2

def test_1():
    s = "cdef"
    assert minAnagramLength(s) == 4

def test_2():
    s = "xxe"
    assert minAnagramLength(s) == 3

def test_3():
    s = "pqqppqpqpq"
    assert minAnagramLength(s) == 2

if __name__ == '__main__':
    test_3()
    test_0()
    test_1()
    test_2()


