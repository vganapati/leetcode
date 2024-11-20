"""
https://neetcode.io/problems/search-2d-matrix
"""

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search the rows

        pointer_0 = 0
        pointer_1 = len(matrix) - 1
        row_ind = 0
        
        while pointer_1 >= pointer_0:
            mid = (pointer_0 + pointer_1)//2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                pointer_1 = mid - 1
            elif matrix[mid][0] < target:
                pointer_0 = mid + 1
                row_ind = mid 

        # row_ind should point to the row of interest

        pointer_0 = 0
        pointer_1 = len(matrix[0]) - 1

        while pointer_1 >= pointer_0:
            mid = (pointer_0 + pointer_1)//2
            if matrix[row_ind][mid] == target:
                return True
            if matrix[row_ind][mid] < target:
                pointer_0 = mid + 1
            else:
                pointer_1 = mid - 1
        
        return False

solution = Solution()

matrix=[[1],[3]]; target=3
assert solution.searchMatrix(matrix, target) == True

matrix = [[1]]; target=2
assert solution.searchMatrix(matrix, target) == False

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]; target = 10
assert solution.searchMatrix(matrix, target) == True

matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]; target = 15
assert solution.searchMatrix(matrix, target) == False