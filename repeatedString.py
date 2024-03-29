def repeatedString(s, n):
    remainder = n % len(s)
    string_a = 0
    prefix_a = 0
    for ind, char in enumerate(s):
        if char == 'a':
            string_a += 1
            if ind < remainder:
                prefix_a += 1
    return string_a*(n//len(s)) + prefix_a

def test_0():
    s = 'abcac'
    n = 10
    assert repeatedString(s, n) == 4

def test_1():
    s = 'aba'
    n = 10
    assert repeatedString(s, n) == 7

if __name__ == "__main__":
    test_0()
    test_1()