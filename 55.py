import numpy as np

def canJump_0(nums):
    accessible_inds = [False]*len(nums)
    accessible_inds[0] = True
    for ind, num in enumerate(nums):
        if accessible_inds[ind]==True:
            accessible_inds[ind:ind+num+1]=[True]*len(accessible_inds[ind:ind+num+1])
        
    return accessible_inds[-1]

def canJump_no_numpy(nums):
    accessible_inds = [False]*len(nums)
    accessible_inds[0] = True
    added_inds_prev = [0]
    
    while len(added_inds_prev)>0 and not(accessible_inds[-1]):
        added_inds_current = []
        for ind in added_inds_prev:
            num = nums[ind]
            if sum(accessible_inds[ind:ind+num+1]) == len(accessible_inds[ind:ind+num+1]):
                pass
            else:
                [added_inds_current.append(i+ind) for i in range(len(accessible_inds[ind:ind+num+1])) if accessible_inds[ind:ind+num+1][i] is False]
            accessible_inds[ind:ind+num+1] = [True]*(num+1)
        added_inds_prev = added_inds_current
        
    return accessible_inds[-1]


def canJump(nums):
    accessible_inds = np.zeros([len(nums),], dtype=bool)
    accessible_inds[0] = True
    for ind, num in enumerate(nums):
        if accessible_inds[ind]==True:
            accessible_inds[ind:ind+num+1]=True
        
    return accessible_inds[-1]


def test_0():
    nums = [2,3,1,1,4]
    assert canJump(nums)==True

def test_1():
    nums = [3,2,1,0,4]
    assert canJump(nums)==False

def test_2():
    nums = [1,2,3]
    assert canJump(nums)==True

if __name__ == '__main__':

    test_2()
    test_0()
    test_1()