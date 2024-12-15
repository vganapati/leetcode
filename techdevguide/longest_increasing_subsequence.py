"""
https://leetcode.com/problems/longest-increasing-subsequence/description/
"""
from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sorted_nums = []
        
        for num in nums:
            # find insertion index into sorted_nums, must be before any repeat
            ind = bisect.bisect_left(sorted_nums, num)
            if ind==len(sorted_nums):
                sorted_nums.append(num)
            else:
                sorted_nums[ind] = num
        return len(sorted_nums)


solution = Solution()
nums = [10,9,2,5,3,7,101,18]
assert solution.lengthOfLIS(nums) == 4

nums = [0,1,0,3,2,3]
assert solution.lengthOfLIS(nums) == 4

nums = [7,7,7,7,7,7,7]
assert solution.lengthOfLIS(nums) == 1