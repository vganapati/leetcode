def sumOfTheDigitsOfHarshadNumber(x):
    x_0 = x
    i = 1
    digit_sum = 0
    while x > 0:
        digit_sum += x % 10
        x = (x - digit_sum)//10
        i += 1
    if x_0 % digit_sum == 0:
        return digit_sum
    else:
        return -1

def test_0():
    x = 18
    assert sumOfTheDigitsOfHarshadNumber(x) == 9

def test_1():
    x = 23
    assert sumOfTheDigitsOfHarshadNumber(x) == -1

if __name__ == '__main__':
    test_0()
    test_1()