def jumpingOnClouds(c):
    if len(c) == 2:
        return 1
    elif len(c) <= 1:
        return 0
    else:
        if c[1] == 1: # must jump over
            return 1+ jumpingOnClouds(c[2:])
        elif c[2] == 1: # cannot jump to position 2
            return 1 + jumpingOnClouds(c[1:])
        else: # make decision
            return min(1+ jumpingOnClouds(c[2:]), 1+ jumpingOnClouds(c[1:]))

def test_0():
    c = [0, 1, 0, 0, 0, 1, 0]
    assert jumpingOnClouds(c) == 3

def test_1():
    c = [0, 0, 1, 0, 0, 1, 0]
    assert jumpingOnClouds(c) == 4

if __name__ == '__main__':
    test_0()
    test_1()