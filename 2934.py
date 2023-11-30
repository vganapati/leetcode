def minOperations(nums1, nums2):
    last_num_1 = nums1[-1]
    last_num_2 = nums2[-1]
    harmless_swaps = 0
    swaps = 0
    for ind in range(len(nums1)-1):
        num_1 = nums1[ind]
        num_2 = nums2[ind]
        if num_1 <= last_num_1 and num_1 <= last_num_2 and num_2 <= last_num_1 and num_2 <= last_num_2:
            harmless_swaps += 1
        elif num_1 <= last_num_2 and num_2 <= last_num_1:
            swaps += 1
        elif num_1 <= last_num_1 and num_2 <= last_num_2 and (num_1 > last_num_2 or num_2 > last_num_1):
            pass # no swap possible
        else:
            return -1

    return min(len(nums1)-swaps-harmless_swaps,swaps)

def test_0():
    nums1 = [1,2,7]
    nums2 = [4,5,3]
    assert minOperations(nums1, nums2) == 1

def test_1():
    nums1 = [2,3,4,5,9]
    nums2 = [8,8,4,4,4]
    assert minOperations(nums1, nums2) == 2

def test_2():
    nums1 = [1,5,4]
    nums2 = [2,5,3]
    assert minOperations(nums1, nums2) == -1

def test_3():
    nums1 = [1,2]
    nums2 = [2,1]
    assert minOperations(nums1, nums2) == 1

if __name__ == '__main__':
    test_0()
    test_1()
    test_2()
    test_3()