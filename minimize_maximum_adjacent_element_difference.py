from typing import List

"""
https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/description/
"""

from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        smallest_val = 10**9 + 1
        largest_val = 1
        maxDiff = 0
        for i, num in enumerate(nums[:-1]):
            if nums[i]==-1 or nums[i+1]==-1:
                if nums[i]>0:
                    smallest_val = min(smallest_val, nums[i])
                    largest_val = max(largest_val, nums[i])
                if nums[i+1]>0:
                    smallest_val = min(smallest_val, nums[i+1])
                    largest_val = max(largest_val, nums[i+1])                    
            else:
                maxDiff = max(maxDiff, 2*abs(nums[i+1]-nums[i]))

        # for i in range(len(nums)):
            

        pointer_2 = 0
        while pointer_2<(len(nums)-1) and nums[pointer_2]==-1:
            pointer_2 += 1
        
        if pointer_2 == len(nums)-1:
            return 0

        if pointer_2 > 0:
            maxDiff = max(maxDiff,min(abs(smallest_val-nums[pointer_2]), abs(largest_val-nums[pointer_2])))
        
        pointer_1 = pointer_2
        pointer_2 = pointer_2+1
        two_thirds = ((largest_val - smallest_val + 2)//3)*2 # +2 for ceiling
        while pointer_2 < len(nums):
            if nums[pointer_2] == -1:
                pointer_2 += 1
            else:
                pointer_diff = pointer_2 - pointer_1
                if pointer_diff==1:
                    pointer_1 += 1
                    pointer_2 += 1
                elif pointer_diff==2:
                    smallest_val_0 = min(nums[pointer_2],nums[pointer_1])
                    largest_val_0 = max(nums[pointer_2],nums[pointer_1])
                    maxDiff = max(maxDiff, min(largest_val-smallest_val_0, largest_val_0 - smallest_val))
                    pointer_1 = pointer_2
                    pointer_2 += 1
                elif pointer_diff > 2:
                    smallest_val_0 = min(nums[pointer_2],nums[pointer_1])
                    largest_val_0 = max(nums[pointer_2],nums[pointer_1])
                    maxDiff = max(maxDiff, min(largest_val-smallest_val_0, largest_val_0 - smallest_val, two_thirds))   
                    pointer_1 = pointer_2
                    pointer_2 += 1
        
        if nums[pointer_2-1] == -1:
            maxDiff = max(maxDiff, min(abs(smallest_val-nums[pointer_1]), abs(largest_val-nums[pointer_1])))
        return (maxDiff+1)//2

solution = Solution()
assert solution.minDifference([-1,-1,-1]) == 0
assert solution.minDifference([1,12]) == 11
assert solution.minDifference([1,2,-1,10,8]) == 4
assert solution.minDifference([29,-1,-1]) == 0
assert solution.minDifference([14,-1]) == 0


assert solution.minDifference([-1,10,-1,8]) == 1