"""
https://leetcode.com/problems/unique-paths-ii/description/
"""

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[rows-1][cols-1] == 1:
            return 0

        memo = [[0]*cols for _ in range(rows)]
        memo[rows-1][cols-1] = 1 

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if obstacleGrid[i][j] == 1 or (i==rows-1 and j==cols-1):
                    pass
                else:
                    bottom = memo[i+1][j] if i<(rows-1) else 0
                    right = memo[i][j+1] if j<(cols-1) else 0
                    memo[i][j] = bottom + right
        return memo[0][0]

solution = Solution()

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
assert solution.uniquePathsWithObstacles(obstacleGrid) == 2

obstacleGrid = [[0,1],[0,0]]
assert solution.uniquePathsWithObstacles(obstacleGrid) == 1