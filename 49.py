def groupAnagrams(strs):
    anagrams_dict = {}
    for str in strs:
        try:
            anagrams_dict["".join(sorted(str))].append(str)
        except KeyError:
            anagrams_dict["".join(sorted(str))] = [str]
    anagrams_vec = []
    for key in anagrams_dict.keys():
        anagrams_vec.append(anagrams_dict[key])
    
    return anagrams_vec

def test_0():
    assert groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [["bat"],["nat","tan"],["ate","eat","tea"]]

def test_1():
    assert groupAnagrams([""]) == [[""]]

def test_2():
    assert groupAnagrams(["a"]) == [["a"]]

if __name__ == "__main__":
    # test_0()
    test_1()
    test_2()