"""
https://leetcode.com/problems/subsets-ii/description/
"""
from typing import List

class Solution:
    def subsetWithDup(self, nums: List[int]) -> List[List[int]]:
        def subsetWithDup_0(ind):
            if len(nums) == ind:
                return [[]], 1
            
            sub_subsets_0, num_prev_added = subsetWithDup_0(ind+1)
            if (ind+1)<len(nums) and nums[ind+1] == nums[ind]:
                sub_subsets_1 = [[nums[ind]]+i for i in sub_subsets_0[len(sub_subsets_0)-num_prev_added:]]
                output = sub_subsets_0 + sub_subsets_1
            else:
                sub_subsets_1 = [[nums[ind]]+i for i in sub_subsets_0]
                output = sub_subsets_0 + sub_subsets_1
            return output, len(sub_subsets_1)
        
        nums.sort()
        return subsetWithDup_0(0)[0]

solution = Solution()
print(solution.subsetWithDup([1,2,2,2]))