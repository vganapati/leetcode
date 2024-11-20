"""
https://neetcode.io/problems/eating-bananas
"""

from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowest_speed = 1
        highest_speed = max(piles)
        
        lowest_possible = highest_speed

        while highest_speed >= lowest_speed:
            mid_speed = (lowest_speed + highest_speed)//2
            finish_time = 0
            for pile in piles:
                finish_time += pile//mid_speed + int((pile % mid_speed) > 0)
            if finish_time <= h:
                lowest_possible = mid_speed
                highest_speed = mid_speed - 1
            elif finish_time > h:
                lowest_speed = mid_speed + 1
        return lowest_possible



solution = Solution()

piles = [1,4,3,2]; h = 9
assert solution.minEatingSpeed(piles, h) == 2


piles = [25,10,23,4]; h = 4
assert solution.minEatingSpeed(piles, h) == 25

