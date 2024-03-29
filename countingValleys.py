def countingValleys(steps, path):
    current_elevation = 0
    num_valleys = 0
    for step in range(steps):
        previous_elevation = current_elevation
        if path[step] == 'D':
            current_elevation -= 1
        elif path[step] == 'U':
            current_elevation += 1
        else:
            raise NotImplementedError("Not a valid step description")
        if previous_elevation == 0 and current_elevation == -1:
            num_valleys += 1
    return num_valleys

def test_0():
    steps = 8
    path = 'UDDDUDUU'
    assert countingValleys(steps, path) == 1

def test_1():
    steps = 12
    path = 'DDUUDDUDUUUD'
    assert countingValleys(steps, path) == 2

if __name__ == '__main__':
    test_0()
    test_1()
