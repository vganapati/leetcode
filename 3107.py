def minOperationsToMakeMedianK_0(nums, k):
    target_center_ind = len(nums)//2
    nums = sorted(nums)
    lower = []
    middle = 0
    while len(nums) > 0 and nums[0] <= k:
        if nums[0] < k:
            lower.append(nums.pop(0))
        elif nums[0] == k:
            nums.pop(0)
            middle += 1

    operations = 0
    while not(len(lower) <= target_center_ind and len(lower) + middle >= target_center_ind + 1):
        if len(lower) > target_center_ind:
            middle += 1
            num = lower.pop()
            operations += k - num
        elif len(lower) + middle < target_center_ind + 1:
            middle += 1
            num = nums.pop(0)
            operations += num - k
    return operations


def minOperationsToMakeMedianK(nums, k):
    nums = sorted(nums)
    median_ind = len(nums)//2
    operations = 0
    if nums[median_ind] == k:
        return operations
    elif nums[median_ind] < k:
        for num in nums[median_ind:]:
            if num >= k:
                break
            else:
                operations += k-num
    elif nums[median_ind] > k:
        for num in reversed(nums[:median_ind+1]):
            if num <= k:
                break
            else:
                operations += num - k
    return operations

def test_0():
    nums = [2,5,6,8,5]; k = 4
    assert minOperationsToMakeMedianK(nums, k) == 2

def test_1():
    nums = [2,5,6,8,5]; k = 7
    assert minOperationsToMakeMedianK(nums, k) == 3

def test_2():
    nums = [1,2,3,4,5,6]; k = 4
    assert minOperationsToMakeMedianK(nums, k) == 0

if __name__ == '__main__':
    test_1()
    test_0()
    
    test_2()