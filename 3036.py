import numpy as np

def countMatchingSubarrays(nums, pattern):
    lps = processPattern(pattern)
    nums = np.array(nums)
    pattern = np.array(pattern)
    nums = nums[1:] - nums[:-1]
    nums[nums<0] = -1
    nums[nums>0] = 1
    count = 0
    i = 0
    j_start = 0
    while i < len(nums)-(len(pattern)-j_start-1):
        mismatch = False
        for j in range(j_start, len(pattern)):
            if nums[i] != pattern[j]:
                mismatch = True
                if j == 0:
                    j_start = 0
                    i = i+1
                else:
                    j_start = lps[j-1]
                break
            i += 1
            
        if not mismatch:
            count += 1
            j_start = lps[j]
    return count

def processPattern(pattern):
    lps = [0]*len(pattern)
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            lps[j] = i + 1
            i += 1
            j += 1
        else:
            if i == 0:
                lps[j] = 0
                j += 1
            else:
                i = lps[i-1]
    return lps

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

def test_4():
    nums = [107130569,107130569,147942552,147942552,370036210]; pattern = [1,0,1]
    assert countMatchingSubarrays(nums, pattern) == 1

def test_5():
    nums = [279383512,279383512,682964660,706808559,858592395,858592395]; pattern = [0,1,1,1]
    assert countMatchingSubarrays(nums, pattern) == 1

def test_6():
    nums = [175027954,2959950,175027954,278021869,175027954,278021869,293580800,512709790,293580800,512709790,583759803,729769133,583759803,729769133,893799515,895479711]
    pattern = [1,1,-1,1,1,1,-1,1]
    assert countMatchingSubarrays(nums, pattern) == 2

if __name__ == '__main__':
    test_6()
    test_5()
    test_4()
    test_2()
    test_0()
    test_1()
    test_3()