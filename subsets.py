"""
https://leetcode.com/problems/subsets/description/
"""

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]
        
        output = []

        sub_subsets = self.subsets(nums[1:])
        output += sub_subsets
        output += [[nums[0]] + i for i in sub_subsets]
        
        return output

solution = Solution()

nums = [1,2,3]
print(solution.subsets(nums))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


nums = [0]
print(solution.subsets(nums)) # [[],[0]]