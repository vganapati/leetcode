import numpy as np

def minSubArrayLen(target, nums):

    if sum(nums) < target:
        return 0
    elif sum(nums)==target:
        return len(nums)
    elif max(nums)>=target:
        return 1

    left_pointer = 0
    right_pointer = 1
    smallest_count = len(nums)
    current_sum = sum(nums[left_pointer:right_pointer])
    while left_pointer < right_pointer and right_pointer<=len(nums):
        if current_sum >= target:
            smallest_count = min(smallest_count, len(nums[left_pointer:right_pointer]))
            current_sum -= nums[left_pointer]
            left_pointer += 1
        else:
            try:
                current_sum += nums[right_pointer]
            except IndexError:
                pass
            right_pointer += 1
    return smallest_count



def test_0():
    assert minSubArrayLen(7, [2,3,1,2,4,3]) == 2

def test_1():
    assert minSubArrayLen(4, [1,4,4]) == 1

def test_2():
    assert minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0



if __name__ == "__main__":
    test_0()
    test_1()
    test_2()