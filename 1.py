from typing import List
from collections import defaultdict

def twoSum(nums: List[int], target: int) -> List[int]:
    pairs = defaultdict(lambda:None)

    for ind, num in enumerate(nums):
        complement = target - num
        if pairs[complement] is not None:
            return [pairs[complement], ind]
        else:
            pairs[num] = ind


def test_0():
    nums = [2,7,11,15]; target = 9
    assert twoSum(nums, target) == [0,1]

def test_1():
    nums = [3,2,4]; target = 6
    assert twoSum(nums, target) == [1,2]

if __name__ == '__main__':
    test_0()
    test_1()