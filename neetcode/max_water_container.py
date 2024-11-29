from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pointer_0 = 0
        pointer_1 = len(heights)-1
        area = 0

        while pointer_1 > pointer_0:
            area_i = min(heights[pointer_0], heights[pointer_1])*(pointer_1 - pointer_0)
            area = max(area, area_i)

            # move limiting pointer
            if heights[pointer_0] < heights[pointer_1]:
                pointer_0 += 1
            else:
                pointer_1 -= 1
        
        return area

solution = Solution()

height = [1,7,2,5,4,7,3,6]
assert solution.maxArea(height) == 36

height = [2,2,2]
assert solution.maxArea(height) == 4


