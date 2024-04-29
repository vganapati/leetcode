def addedInteger(nums1, nums2):
    return min(nums2) - min(nums1)


def test_0():
    nums1 = [2,6,4]; nums2 = [9,7,5]
    assert addedInteger(nums1, nums2) == 3

def test_1():
    nums1 = [10]; nums2 = [5]
    assert addedInteger(nums1, nums2) == -5

def test_2():
    nums1 = [1,1,1,1]; nums2 = [1,1,1,1]
    assert addedInteger(nums1, nums2) == 0

if __name__ == '__main__':
    test_0()
    test_1()
    test_2()