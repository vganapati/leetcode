"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/
"""

from typing import List
import bisect

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)

        counts = []
        for num in nums:
            ind = bisect.bisect_left(nums_sorted, num)
            counts.append(ind)
            nums_sorted.pop(ind)
        return counts


solution = Solution()

nums = [5,2,6,1]
assert solution.countSmaller(nums) == [2,1,1,0]

nums = [-1]
assert solution.countSmaller(nums) == [0]

nums = [-1,-1]
assert solution.countSmaller(nums) == [0,0]