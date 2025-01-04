"""
https://leetcode.com/problems/where-will-the-ball-fall/description/?envType=problem-list-v2&envId=50izszui
"""

from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])

        grid_top = [[0]*cols for _ in range(rows)] # where ball goes if in top of cell
        grid_bottom = [[0]*cols for _ in range(rows)] # where ball goes if in bottom of cell

        # 0 represents wall
        for i in range(rows-1,-1,-1):
            for j in range(cols):
                grid_bottom[i][j] = grid_top[i+1][j] if i<(rows-1) else j

            for j in range(cols):
                curr = grid[i][j]
                left = grid[i][j-1] if j>0 else 0
                right = grid[i][j+1] if j<(cols-1) else 0

                if curr == -1 and left == -1:
                    grid_top[i][j] = grid_bottom[i][j-1]
                elif curr == -1 and (left == 0 or left == 1):
                    grid_top[i][j] = -1
                
                if curr == 1 and right == 1:
                    grid_top[i][j] = grid_bottom[i][j+1]
                elif curr == 1 and (right == -1 or right == 0):
                    grid_top[i][j] = -1
        
        return grid_top[0]


solution = Solution()

grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
assert solution.findBall(grid) == [1,-1,-1,-1,-1]

grid = [[-1]]
assert solution.findBall(grid) == [-1]

grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
assert solution.findBall(grid) == [0,1,2,3,4,-1]