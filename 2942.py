def findWordsContaining(words, x):
    indices = []
    for ind, word in enumerate(words):
        if x in word:
            indices.append(ind)
    return(indices)

def test_0():
    words = ["leet","code"]
    x = "e"
    assert set(findWordsContaining(words,x))==set([0,1])

def test_1():
    words = ["abc","bcd","aaaa","cbc"]
    x = "a"
    assert set(findWordsContaining(words,x))==set([0,2])

def test_2():
    words = ["abc","bcd","aaaa","cbc"]
    x = "z"
    assert set(findWordsContaining(words,x))==set([])

if __name__ == '__main__':
    test_0()
    test_1()
    test_2()