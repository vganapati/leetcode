def countAlternatingSubarrays(nums):
    subarray_count = [1]*len(nums)
    for ind, val in enumerate(nums):
        if ind == 0:
            pass
        else:
            subarray_max_len = ind + 1
            if val != nums[ind-1]:
                subarray_count[ind] += subarray_count[ind-1]
    return sum(subarray_count)

def test_0():
    nums = [0,1,1,1]
    assert countAlternatingSubarrays(nums) == 5

def test_1():
    nums = [1,0,1,0]
    assert countAlternatingSubarrays(nums) == 10

if __name__ == '__main__':
    test_0()
    test_1()
    