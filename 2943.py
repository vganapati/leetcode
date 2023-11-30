def findMaxSequential(hBars):
    hBars.sort()
    max_sequential_h = 0
    h_previous = hBars[0]
    sequential_current = 1
    
    for h in hBars[1:]:
        if h == h_previous+1:
            sequential_current += 1
        else:
            max_sequential_h = max(max_sequential_h, sequential_current)
            sequential_current = 1
        h_previous = h
    max_sequential_h = max(max_sequential_h, sequential_current)
    return(max_sequential_h)

def maximizeSquareHoleArea(n, m, hBars, vBars):

    max_sequential_h = findMaxSequential(hBars)
    max_sequential_v = findMaxSequential(vBars)

    return((min(max_sequential_h, max_sequential_v)+1)**2)

def test_3():
    n = 4; m = 40; hBars = [5,3,2,4]; vBars = [36,41,6,34,33]
    assert maximizeSquareHoleArea(n, m, hBars, vBars) == 9

def test_0():
    n = 2; m = 1; hBars = [2,3]; vBars = [2]
    assert maximizeSquareHoleArea(n, m, hBars, vBars) == 4

def test_1():
    n = 1; m = 1; hBars = [2]; vBars = [2]
    assert maximizeSquareHoleArea(n, m, hBars, vBars) == 4

def test_2():
    n = 2; m = 3; hBars = [2,3]; vBars = [2,3,4]
    assert maximizeSquareHoleArea(n, m, hBars, vBars) == 9



if __name__ == '__main__':
    test_3()
    test_0()
    test_1()
    test_2()
    