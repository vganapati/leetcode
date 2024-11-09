from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix = 0
        max_val = nums[0]

        for num in nums:
            if prefix < 0:
                prefix = 0 # throw it out
            prefix += num
            max_val = max(max_val, prefix)
        return max_val
        




if __name__ == '__main__':
    solution = Solution()
    assert solution.maxSubArray([8,-19,5,-4,20]) == 21
    assert solution.maxSubArray([2,-3,4,-2,2,1,-1,4]) == 8
    assert solution.maxSubArray([-1]) == -1