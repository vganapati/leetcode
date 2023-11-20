def maximumStrongPairXor(nums):
    nums.sort()
    max_xor = 0
    for ind_0,num_0 in enumerate(nums):
        print(ind_0)
        for ind_1, num_1 in enumerate(nums[ind_0:]):
            if (num_1-num_0) > num_0:
                break
            max_xor = max(num_0 ^ num_1, max_xor)
    return(max_xor)

def test_0():
    nums = [1,2,3,4,5]
    assert maximumStrongPairXor(nums) == 7

def test_1():
    nums = [10,100]
    assert maximumStrongPairXor(nums) == 0

def test_2():
    nums = [5,6,25,30]
    assert maximumStrongPairXor(nums) == 7

if __name__ == '__main__':
    test_0()
    test_1()
    test_2()