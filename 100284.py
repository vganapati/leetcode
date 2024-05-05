def isValid(word):
    if len(word) < 3:
        return False
    
    vowel = False
    consonant = False
    vowels = set([65, 69, 73, 79, 85, 97, 101, 105, 111, 117])
    valid_alpha = list(range(65,91)) + list(range(97,123))
    valid_ord = list(range(48,58)) + valid_alpha # numbers and letters

    valid_alpha = set(valid_alpha)
    valid_ord = set(valid_ord)

    for character in word:
        ascii_code = ord(character)
        if ascii_code not in valid_ord:
            return False
        else:
            if ascii_code in valid_alpha:
                if ascii_code in vowels:
                    vowel = True
                else:
                    consonant = True
    
    if vowel and consonant:
        return True
    else:
        return False


def test_0():
    word = "234Adas"
    assert isValid(word) == True

def test_1():
    word = "b3"
    assert isValid(word) == False

def test_2():
    word = "a3$e"
    assert isValid(word) == False

def test_3():
    word = "xiUz"
    assert isValid(word) == True

if __name__ == '__main__':
    test_0()
    test_1()
    test_2()
    test_3()