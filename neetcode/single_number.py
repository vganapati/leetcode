from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        for ind, num in enumerate(nums):
            if ind == 0:
                single = num
            else:
                single = single ^ num
        
        return single

