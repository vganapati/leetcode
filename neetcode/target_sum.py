"""
https://neetcode.io/problems/target-sum
https://leetcode.com/problems/target-sum/description/
"""

from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        previous_memo = defaultdict(int) # key is the curr_sum, value is the number of ways to get there
        previous_memo[0] = 1

        for pointer in range(len(nums)):
            curr_val = nums[pointer]
            curr_memo = defaultdict(int)
            for key in previous_memo.keys():
                count = previous_memo[key]
                curr_memo[key-curr_val] += count
                curr_memo[key+curr_val] += count
            previous_memo = curr_memo
        
        return curr_memo[target]

solution = Solution()
nums = [1,1,1,1,1]; target = 3
assert solution.findTargetSumWays(nums, target) == 5

nums = [1]; target = 1
assert solution.findTargetSumWays(nums, target) == 1