def longestMonotonicSubarray(nums):
    previous_increase_len = 0
    current_increase_len = 0
    increasing = False

    previous_decrease_len = 0
    current_decrease_len = 0
    decreasing = False

    for ind, num in enumerate(nums):
        if ind == 0:
            previous_num = num
        else:
            if num > previous_num:
                if increasing:
                    current_increase_len += 1
                if decreasing:
                    if current_decrease_len > previous_decrease_len:
                        previous_decrease_len = current_decrease_len
                        current_decrease_len = 0
                    increasing = True
                    decreasing = False
                    current_increase_len = 1
                if not(increasing) and not(decreasing):
                    current_increase_len = 1
                    increasing = True
            elif num < previous_num:
                if decreasing:
                    current_decrease_len += 1
                if increasing:
                    if current_increase_len > previous_increase_len:
                        previous_increase_len = current_increase_len
                        current_increase_len = 0
                    increasing = False
                    decreasing = True
                    current_decrease_len = 1
                if not(increasing) and not(decreasing):
                    current_decrease_len = 1
                    decreasing = True
            elif num == previous_num:
                if decreasing:
                        if current_decrease_len > previous_decrease_len:
                            previous_decrease_len = current_decrease_len
                            current_decrease_len = 0
                if increasing:
                    if current_increase_len > previous_increase_len:
                        previous_increase_len = current_increase_len
                        current_increase_len = 0
                increasing = False
                decreasing = False
            previous_num = num
    return 1+max(current_decrease_len, previous_decrease_len, current_increase_len, previous_increase_len)

def test_0():
    nums = [1,4,3,3,2]
    assert longestMonotonicSubarray(nums) == 2

def test_1():
    nums = [3,3,3,3]
    assert longestMonotonicSubarray(nums) == 1

def test_2():
    nums = [3,2,1]
    assert longestMonotonicSubarray(nums) == 3

def test_3():
    nums = [1,10,10]
    assert longestMonotonicSubarray(nums) == 2

if __name__ == '__main__':
    test_3()
    test_0()
    test_1()
    test_2()