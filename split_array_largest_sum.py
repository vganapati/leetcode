from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        min_val = float("inf")
        for num in nums:
            min_val = min(min_val, num)

        max_val = float("-inf")
        pieces = len(nums)//k
        for i in range(k):
            if i == k-1:
                sum_i = sum(nums[i*pieces:])
            else:
                sum_i = sum(nums[i*pieces:(i+1)*pieces])
            max_val = max(max_val, sum_i)
        
        # binary search in between min_val and max_val
        pointer_0 = min_val
        pointer_1 = max_val

        while pointer_1>pointer_0:
            mid_val = (pointer_1 + pointer_0)//2            
            # can mid_val be formed?
            ind = 0
            for i in range(k):
                sum_i = 0
                while sum_i <= mid_val and ind<len(nums):
                    sum_i += nums[ind]
                    ind += 1
                ind -= 1
            if sum_i > mid_val: # last sum exceeds mid_val
                # fail
                pointer_0 = mid_val + 1
            else:
                pointer_1 = mid_val
        
        return pointer_1
            


solution = Solution()
nums = [7,2,5,10,8]; k = 2
assert solution.splitArray(nums, k) == 18

nums = [1,2,3,4,5]; k = 2
assert solution.splitArray(nums, k) == 9