def uniquePaths(m, n):
    x = max(m,n)-1
    y = min(m,n)-1
    result = 1.0
    for ind,num in enumerate(range(x+1,x+y+1)):
        result *= num
        result /= (ind+1)
    return int(result)

def test_0():
    assert uniquePaths(3,7) == 28

def test_1():
    assert uniquePaths(3,2) == 3

if __name__ == '__main__':
    test_0()
    test_1()