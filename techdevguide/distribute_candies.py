"""
https://leetcode.com/problems/distribute-candies/description/
"""

from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        num_types = len(set(candyType))
        if num_types <= len(candyType)//2:
            return num_types
        else:
            return len(candyType)//2

solution = Solution()

candyType = [1,1,2,2,3,3]
assert solution.distributeCandies(candyType) == 3

candyType = [1,1,2,3]
assert solution.distributeCandies(candyType) == 2

candyType = [6,6,6,6]
assert solution.distributeCandies(candyType) == 1