"""
https://neetcode.io/problems/largest-rectangle-in-histogram
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        height_stack = []
        for ind, height in enumerate(heights):
            ind_pop = ind
            while height_stack and height_stack[-1][1]>height:
                ind_pop, height_pop = height_stack.pop()
                maxArea = max(maxArea, height_pop*(ind-ind_pop)) 
            height_stack.append([ind_pop,height])
        while height_stack:
            ind_pop, height_pop = height_stack.pop()
            maxArea = max(maxArea, height_pop*(len(heights)-ind_pop))
        return maxArea



solution = Solution()
assert solution.largestRectangleArea([7,1,7,2,2,4]) == 8
assert solution.largestRectangleArea([1,3,7]) == 7
assert solution.largestRectangleArea([10]) == 10
assert solution.largestRectangleArea([0]) == 0
assert solution.largestRectangleArea([1,2,3,4,5]) == 9
assert solution.largestRectangleArea([5,4,3,2,1]) == 9