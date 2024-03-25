def maximumLengthSubstring(s):
    max_length = 2
    ind_0 = 0
    flag = True

    while max_length < len(s)-ind_0 and flag:
        char_dict = {}
        current_window = 0
        flag = True
        for ind_1, char_1 in enumerate(s[ind_0:]):
            try:
                char_dict[char_1] += [ind_1 + ind_0]
            except KeyError:
                char_dict[char_1] = [ind_1 + ind_0]
            if len(char_dict[char_1]) > 2:
                ind_0 = char_dict[char_1].pop(0) + 1
                flag = True 
                break
            else:
                flag = False
                current_window += 1
                if current_window > max_length:
                    max_length = current_window
    return max_length



def test_0():
    s = "bcbbbcba"
    assert maximumLengthSubstring(s) == 4

def test_1():
     s = "aaaa"
     assert maximumLengthSubstring(s) == 2

if __name__ == "__main__":
    test_0()
    test_1()