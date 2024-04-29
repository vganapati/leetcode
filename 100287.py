import numpy as np
def minimumAddedInteger(nums1, nums2):
    nums1.sort()
    nums2.sort()

    diff = 10000
    for i in range(3):
        diff_i = nums2[0] - nums1[i]
        if diff_i < diff:
            offset = 0
            flag = True
            ind = 0
            while flag and ind < len(nums2):
                if diff_i != (nums2[ind] - nums1[ind+offset]):
                    if offset == 2:
                        flag = False
                    else:
                        offset += 1
                else:
                    ind += 1

            if flag:
                diff = diff_i
    return diff

def test_0():
    nums1 = [4,20,16,12,8]; nums2 = [14,18,10]
    assert minimumAddedInteger(nums1, nums2) == -2

def test_1():
    nums1 = [3,5,5,3]; nums2 = [7,7]
    assert minimumAddedInteger(nums1, nums2) == 2

if __name__ == '__main__':
    test_0()
    test_1()