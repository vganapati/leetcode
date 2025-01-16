from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # greedy solution
        current_jumps = nums[0]
        for num in nums[1:]:
            current_jumps -= 1
            if current_jumps < 0:
                return False
            if num > current_jumps:
                current_jumps = num
        return True


    def canJump_dynamic(self, nums: List[int]) -> bool:
        # worst case O(n^2) time complexity
        access_last = [False]*len(nums)
        access_last[-1] = True
        for i in range(len(nums)-2,-1,-1):
            for access_ind in range(1,nums[i]+1):
                if access_last[i+access_ind] == True:
                    access_last[i] = True
                    break
        return access_last[0]

solution = Solution()
nums = [3,2,1,0,4]
assert solution.canJump(nums) == False

nums = [2,3,1,1,4]
assert solution.canJump(nums) == True