"""
https://leetcode.com/problems/burst-balloons/description/
"""

from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = {} # tuple of balloons remaining -> coins
        def maxCoins_0(nums):
            if tuple(nums) in memo.keys():
                return memo[tuple(nums)]
            
            if len(nums) == 1:
                coin = nums[0]
                return coin
            
            if len(nums) == 2:
                coin = nums[0]*nums[1] + max(nums[0],nums[1])
                memo[tuple(nums)] = coin
                return coin
            
            coin_vec = []
            for ind in range(len(nums)):
                left = nums[ind-1] if ind>0 else 1
                right = nums[ind+1] if ind<(len(nums)-1) else 1
                coin_i = nums[ind]*left*right + maxCoins_0(nums[:ind]+nums[ind+1:])
                coin_vec.append(coin_i)
            coin = max(coin_vec)
            memo[tuple(nums)] = coin
            return coin
        coin = maxCoins_0(nums)
        return coin
    
solution = Solution()

nums = [2,3,7,9,1,8,2]
assert solution.maxCoins(nums) == 832

nums = [3,1,5,8]
assert solution.maxCoins(nums) == 167

nums = [1,5]
assert solution.maxCoins(nums) == 10