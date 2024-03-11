import functools

@functools.lru_cache(500000)
def getWays_helper(n, c):
    if n == 0:
        return 1
    elif n<0 or c==():
        return 0
    else:
        return getWays_helper(n-c[0],c) + getWays_helper(n,c[1:])

def change(amount,coins):
    return getWays_helper(amount,tuple(coins))

def test_0():
    assert change(3, [8,3,1,2]) == 3

if __name__ == '__main__':
    test_0()