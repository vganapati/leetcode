import numpy as np

def countMatchingSubarrays(nums, pattern):
    nums = np.array(nums)
    pattern = np.array(pattern)
    nums = nums[1:] - nums[:-1]
    nums[nums<0] = -1
    nums[nums>0] = 1
    count = 0
    for i in range(len(nums)-len(pattern)+1):
        if np.all(nums[i:i+len(pattern)] == pattern):
            count += 1
    return count

def test_0():
    nums = [1,2,3,4,5,6]; pattern = [1,1]
    assert countMatchingSubarrays(nums, pattern) == 4

def test_1():
    nums = [1,4,4,1,3,5,5,3]; pattern = [1,0,-1]
    assert countMatchingSubarrays(nums, pattern) == 2

def test_2():
    nums = [604545939,604545939,604545939,481251768]; pattern = [0]
    assert countMatchingSubarrays(nums, pattern) == 2

def test_3():
    nums = [563133167,499489773,499489773,389385364,389385364,389385364]; pattern = [-1,0,-1]
    assert countMatchingSubarrays(nums, pattern) == 1

if __name__ == '__main__':
    test_0()
    test_1()
    test_2()
    test_3()