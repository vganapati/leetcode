def minimumOperationsToMakeKPeriodic(word, k):
    num_subwords = len(word)//k

    if num_subwords == 1:
        return 0
    
    subword_dict = {}

    max_subwords = 1
    for i in range(0,num_subwords):
        subword = word[i*k:(i+1)*k]
        try:
            subword_dict[subword] += 1
            if subword_dict[subword] > max_subwords:
                max_subwords = subword_dict[subword]
        except KeyError:
            subword_dict[subword] = 1
    return(num_subwords - max_subwords)



def test_0():
    word = "leetcodeleet"; k = 4
    assert minimumOperationsToMakeKPeriodic(word, k) == 1

def test_1():
    word = "leetcoleet"; k = 2
    assert minimumOperationsToMakeKPeriodic(word, k) == 3

def test_2():
    word = "xu"; k = 1
    assert minimumOperationsToMakeKPeriodic(word, k) == 1

if __name__ == '__main__':
    test_2()
    test_0()
    test_1()