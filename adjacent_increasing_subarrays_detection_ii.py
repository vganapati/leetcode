from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:

        pointer_1 = 1
        streak = 1
        streak_vec = []
        previous_streak = 0
        max_streak = 1

        while pointer_1 < len(nums):
            if nums[pointer_1] <= nums[pointer_1-1]:
                streak_vec.append(streak)
                max_streak = max(max_streak,streak//2, min(previous_streak,streak))
                previous_streak = streak
                streak = 1
            else:
                streak += 1
            pointer_1 += 1
        streak_vec.append(streak)
        max_streak = max(max_streak,streak//2, min(previous_streak,streak))
        return max_streak
    
if __name__ == '__main__':
    solution = Solution()
    assert solution.maxIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7]) == 2
    assert solution.maxIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1]) == 3
    

