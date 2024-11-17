from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        smallest_val = 10**9 + 1
        largest_val = 1
        pairs = []
        count = 0
        min_pair_ind = 0
        max_pair_ind = 0
        max_diff = 0
        for i, num in enumerate(nums):
            if i<(len(nums)-1):
                dist = abs(nums[i] - nums[i+1])
                max_diff = max(max_diff, dist)
            if num == -1: 
                if i>0 and i<(len(nums)-1):
                    left = nums[i-1]
                    right = nums[i+1]
                else:
                    if i==0:
                        single = nums[i+1]
                    elif i==len(nums)-1:
                        single = nums[i-1]
                    left, right = single,single
                pairs.append([left,right])
                if left < smallest_val:
                    min_pair_ind = count
                    smallest_val = left
                if right < smallest_val:
                    min_pair_ind = count
                    smallest_val = right
                if left > largest_val:
                    max_pair_ind = count
                    largest_val = left
                if right > largest_val:
                    max_pair_ind = count
                    largest_val = right
                count += 1
        breakpoint()
        if count == 0:
            return max_diff
        if min_pair_ind == max_pair_ind:
            left, right = pairs[min_pair_ind]
            dist = abs(left-right)
            return max(max_diff, dist//2 + dist%2)
        
        # interval_0 is starting from smallest_val
        # interval_1 is ending at largest_val

        interval_0_right = smallest_val
        interval_1_left = largest_val

        for left,right in pairs:
            min_i = min(left, right)
            max_i = max(left, right)
            if abs(smallest_val-max_i) < abs(largest_val-min_i):
                # place in interval_0
                interval_0_right = max(interval_0_right, min_i, max_i)
            else:
                interval_1_left = min(interval_1_left, min_i, max_i)
        dist_0 = abs(smallest_val-interval_0_right)
        dist_1 = abs(largest_val-interval_1_left)
        breakpoint()
        return max(dist_0//2 + dist_0%2, dist_1//2 + dist_1%2, max_diff)

solution = Solution()
assert solution.minDifference([29,-1,-1]) == 0
assert solution.minDifference([14,-1]) == 0
assert solution.minDifference([1,12]) == 11
assert solution.minDifference([1,2,-1,10,8]) == 4
assert solution.minDifference([-1,-1,-1]) == 0
assert solution.minDifference([-1,10,-1,8]) == 1