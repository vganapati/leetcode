"""
https://leetcode.com/problems/combination-sum/description/
https://neetcode.io/problems/combination-target-sum
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def combinationSum_0(candidates, target):
            if target == 0:
                return [[]]
            
            combos = []
            for ind, num in enumerate(candidates):
                new_target = target-num
                if new_target>=0:
                    combos += [[num] + i for i in combinationSum_0(candidates[ind:], new_target)]
            return combos

        return combinationSum_0(candidates, target)

solution = Solution()

nums = [5]
target = 4
print(solution.combinationSum(nums, target)) # []


nums = [3,4,5]
target = 16
print(solution.combinationSum(nums, target)) # [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]


nums = [2,5,6,9] 
target = 9
print(solution.combinationSum(nums, target)) # [[2,2,5],[9]]




nums = [3]
target = 5
print(solution.combinationSum(nums, target)) # []
