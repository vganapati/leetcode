from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        val = sum(nums)//2

        sums = set([0])
        for i in range(0,len(nums)):
            new_sums = set()
            for sum_i in sums:
                new_sum = sum_i + nums[i]
                if new_sum == val:
                    return True
                if new_sum < val:
                    new_sums.add(new_sum)
            sums = sums | new_sums

        return False

    def canPartition_0(self, nums: List[int]) -> bool:
        prev_diffs = set([nums[0]])

        for i in range(1,len(nums)):
            curr_diffs = set()
            for diff in prev_diffs:
                diff_0 = abs(nums[i]+diff)
                diff_1 = abs(-nums[i]+diff)
                if i==(len(nums)-1) and (diff_0==0 or diff_1==0):
                    return True
                curr_diffs.add(diff_0)
                curr_diffs.add(diff_1)

            prev_diffs = curr_diffs
        return False



solution = Solution()

nums = [1,5,11,5]
assert solution.canPartition(nums) == True

nums = [1,2,3,5]
assert solution.canPartition(nums) == False
