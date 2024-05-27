def maxDepth(s):
    current_depth = 0
    max_depth = 0
    for character in s:
        if character == "(":
            current_depth += 1
        elif character == ")":
            current_depth -= 1
        if current_depth > max_depth:
            max_depth = current_depth
    return max_depth


def test_0():
    s = "(1+(2*3)+((8)/4))+1"
    assert maxDepth(s) == 3

def test_1():
    s = "(1)+((2))+(((3)))"
    assert maxDepth(s) == 3

def test_2():
    s = "()(())((()()))"
    assert maxDepth(s) == 3

if __name__ == '__main__':
    test_0()
    test_1()
    test_2()