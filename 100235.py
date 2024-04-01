def maxBottlesDrunk(numBottles, numExchange):
    bottlesDrunk = numBottles
    bottlesEmpty = numBottles
    while bottlesEmpty >= numExchange:
        bottlesEmpty -= numExchange
        numExchange += 1
        bottlesDrunk += 1
        bottlesEmpty += 1
    return bottlesDrunk

def test_0():
    numBottles = 13; numExchange = 6
    assert maxBottlesDrunk(numBottles, numExchange) == 15

def test_1():
    numBottles = 10; numExchange = 3
    assert maxBottlesDrunk(numBottles, numExchange) == 13

if __name__ == '__main__':
    test_0()
    test_1()
    