from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass

solution = Solution()
matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
assert solution.searchMatrix(matrix) == True

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
assert solution.searchMatrix(matrix) == False
