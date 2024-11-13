"""
https://neetcode.io/problems/trapping-rain-water
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        def trap_0(height):
            pointer_0 = 0
            height_0 = 0

            pointer_1 = 0

            water = 0

            while pointer_1 < len(height):
                height_1 = height[pointer_1]
                if height[pointer_1] >= height_0:
                    water += (pointer_1 - pointer_0 - 1)*height_0 - sum(height[pointer_0+1:pointer_1])
                    pointer_0 = pointer_1
                    height_0 = height_1
                pointer_1 += 1

            height_new = height[pointer_0:][::-1]
            return water, height_new
        
        # from the other direction

        water_0, height_new = trap_0(height)
        water_1, _ = trap_0(height_new)

        return water_0 + water_1

if __name__ == "__main__":
    solution = Solution()

    height = [0,2,0,3,1,0,1,3,2,1]
    assert solution.trap(height) == 9

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    assert solution.trap(height) == 6
