def removeDigit(number, digit):
    last_occurence_ind = -1
    for ind, n in enumerate(number):
        if n == digit:
            last_occurence_ind = ind
            if ind == len(number)-1:
                return number[:-1]
            else:
                n_0 = int(n)
                n_1 = int(number[ind+1])
                if n_1 > n_0:
                    return number[:ind] + number[ind+1:]
    return number[:last_occurence_ind] + number[last_occurence_ind+1:]

def test_0():
    number = "123"; digit = "3"
    assert removeDigit(number, digit) == "12"

def test_1():
    number = "1231"; digit = "1"
    assert removeDigit(number, digit) == "231"

def test_2():
    number = "551"; digit = "5"
    assert removeDigit(number, digit) == "51"


if __name__ == '__main__':
    test_0()
    test_1()
    test_2()