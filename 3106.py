def getSmallestString(s, k):
    s = list(s)
    for ind in range(len(s)):
        if k <= 0:
            break
        letter = s[ind]
        if letter == 'a':
            pass
        elif k >= 13: # can move to any letter
            s[ind] = 'a'
            k = k - min(ord(letter) - 97, 26 - ord(letter) + 97) 
        else:
            if ord(letter) - 97 - k < 0 or ord(letter) - 97 + k > 25: # we pass 'a'
                s[ind] = 'a'
                k = k - min(ord(letter) - 97, 26 - ord(letter) + 97) 
            else:
                s[ind] = chr(ord(letter) - k)
                k = 0
    return "".join(s)

def test_0():
    s = "zbbz"; k = 3
    assert getSmallestString(s, k) == "aaaz"

def test_1():
    s = "xaxcd"; k = 4
    assert getSmallestString(s, k) == "aawcd"

def test_2():
    s = "lol"; k = 0
    assert getSmallestString(s, k) == "lol"

if __name__ == '__main__':
    test_0()
    test_1()
    test_2()