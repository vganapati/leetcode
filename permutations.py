"""
https://leetcode.com/problems/permutations/description/
"""
from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        output = []
        for ind in range(len(nums)):
            output += [[nums[ind]] + i for i in self.permute(nums[:ind]+nums[ind+1:])]

        return output

solution = Solution()
nums = [1,2,3]
print(solution.permute(nums)) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

nums = [0,1]
print(solution.permute(nums)) # [[0,1],[1,0]]

nums = [1]
print(solution.permute(nums)) # [[1]]