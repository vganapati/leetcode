def isPalindrome(s):
    s = s.lower()
    s = "".join(filter(lambda x: x.isalnum(),s))
    pointer_start = 0
    pointer_end = len(s)-1

    for ind in range(len(s)//2):
        if s[pointer_start] == s[pointer_end]:
            pointer_start += 1
            pointer_end -= 1
        else:
            return False
    return True

def test_0():
    assert isPalindrome("A man, a plan, a canal: Panama") == True

def test_1():
    assert isPalindrome("race a car") == False

def test_2():
    assert isPalindrome(" ") == True

if __name__ == "__main__":
    test_0()
    test_1()
    test_2()