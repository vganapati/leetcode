def stringIndices(wordsContainer, wordsQuery):
    trie = {}
    shortest_word_len = 5e3 + 1
    for word_ind, word in enumerate(wordsContainer):
        word_len = len(word)
        if word_len < shortest_word_len:
            shortest_word_len = word_len
            shortest_word_ind = word_ind
        current_trie = trie
        for char in word[::-1]:
            try: 
                [(word_ind_0, word_len_0), child_trie] = current_trie[char]
                if word_len < word_len_0:
                    current_trie[char] = [(word_ind, word_len),child_trie]
                current_trie = child_trie
            except KeyError:
                current_trie[char] = [(word_ind, word_len),{}]
                current_trie = current_trie[char][1]
    ans = []
    for word in wordsQuery:
        current_trie = trie
        word_ind_i = shortest_word_ind
        word_len_i = shortest_word_len
        for char in word[::-1]:
            try:
                [(word_ind_0, word_len_0), child_trie] = current_trie[char]
                word_ind_i = word_ind_0
                word_len_i = word_len_0
                current_trie = child_trie
            except KeyError:
                break
        ans.append(word_ind_i)

    return ans


def test_0():
    wordsContainer = ["abcd","bcd","xbcd"]; wordsQuery = ["cd","bcd","xyz"]
    assert stringIndices(wordsContainer, wordsQuery) == [1,1,1]

def test_1():
    wordsContainer = ["abcdefgh","poiuygh","ghghgh"]; wordsQuery = ["gh","acbfgh","acbfegh"]
    assert stringIndices(wordsContainer, wordsQuery) == [2,0,2]

if __name__ == "__main__":
    test_0()
    test_1()