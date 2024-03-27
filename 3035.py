def maxPalindromesAfterOperations(words):
    letter_dict = {}
    pairs_needed = []
    for word in words:
        pairs_needed.append(len(word)//2)
        for letter in word:
            try:
                letter_dict[letter] += 1
            except KeyError:
                letter_dict[letter] = 1
    
    # how many pairs do we have?
    total_pairs = 0
    for key in letter_dict.keys():
        total_pairs += letter_dict[key]//2
    
    # fill up pairs from shortest word to longest
    pairs_needed.sort()
    palindromes = 0
    for pair in pairs_needed:
        if total_pairs - pair >= 0:
            palindromes += 1
            total_pairs -= pair
        else:
            break

    return palindromes


def test_0():
    words = ["abbb","ba","aa"]
    assert maxPalindromesAfterOperations(words) == 3

def test_1():
    words = ["abc","ab"]
    assert maxPalindromesAfterOperations(words) == 2

def test_2():
    words = ["cd","ef","a"]
    assert maxPalindromesAfterOperations(words) == 1

if __name__ == '__main__':
    test_0()
    test_1()
    test_2()