import functools

@functools.cache
def climbStairs(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return climbStairs(n-2) + climbStairs(n-1)

def test_0():
    assert climbStairs(2) == 2

def test_1():
    assert climbStairs(3) == 3


if __name__ == '__main__':
    test_0()
    test_1()