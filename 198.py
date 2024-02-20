import functools


def rob(nums):
    @functools.cache
    def rob_tuple(nums):
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        else:
            return max(nums[0]+rob_tuple(nums[2:]), rob_tuple(nums[1:]))
        
    return rob_tuple(tuple(nums))



def test_0():
    assert rob([1,2,3,1]) == 4

def test_1():
    assert rob([2,7,9,3,1]) == 12

if __name__ == '__main__':
    test_0()
    test_1()
