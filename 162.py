import numpy as np
def findPeakElement_0(nums):
    # check endpoints first
    if len(nums)==1 or nums[1]<nums[0]:
        return 0
    elif nums[-1]>nums[-2]:
        return len(nums)-1
    else:
        nums = np.array(nums)
        deriv = np.sign(nums[1:]-nums[:-1])
        ind = np.nonzero((deriv[:-1] + deriv[1:])==0)[0][0] + 1
        return ind
    
def findPeakElement(nums):
    # check endpoints first
    if len(nums)==1 or nums[1]<nums[0]:
        return 0
    elif nums[-1]>nums[-2]:
        return len(nums)-1

    start_ind = 1
    end_ind = len(nums)-2
    while 1:
        mid_ind = (end_ind-start_ind)//2 + start_ind
        if nums[mid_ind]>nums[mid_ind+1] and nums[mid_ind]>nums[mid_ind-1]:
            return mid_ind
        elif nums[mid_ind]<nums[mid_ind+1]:
            start_ind = mid_ind+1
        elif nums[mid_ind]<nums[mid_ind-1]:
            end_ind = mid_ind-1
    
def test_0():
    assert findPeakElement([1,2,3,1])==2

def test_1():
    assert (findPeakElement([1,2,1,3,5,6,4])==5 or findPeakElement([1,2,1,3,5,6,4])==1)

if __name__ == '__main__':
    test_0()
    test_1()