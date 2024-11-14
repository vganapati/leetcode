"""
https://neetcode.io/problems/rotting-fruit
"""
from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        col = len(grid[0])

        freshFruit = 0
        rottedVec = deque()

        for i in range(rows):
            for j in range(col):
                if grid[i][j] == 2:
                    rottedVec.append([i,j])
                elif grid[i][j] == 1:
                    freshFruit += 1
        
        time = 0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while rottedVec and freshFruit>0:
            time += 1
            initLen = len(rottedVec)
            for ind in range(initLen):
                i,j = rottedVec.popleft()
                for dir in directions:
                    i_new, j_new = i + dir[0], j + dir[1]
                    if i_new < rows and i_new >= 0 and j_new < col and j_new >= 0:
                        if grid[i_new][j_new] == 1:
                            grid[i_new][j_new] = 2
                            rottedVec.append([i_new, j_new])
                            freshFruit -= 1
        if freshFruit == 0:
            return time
        elif freshFruit > 0:
            return -1
        else:
            raise Exception("freshFruit should not go negative")

solution = Solution()
assert solution.orangesRotting([[1,1,0],[0,1,1],[0,1,2]]) == 4
assert solution.orangesRotting([[1,0,1],[0,2,0],[1,0,1]]) == -1
assert solution.orangesRotting([[2]]) == 0
assert solution.orangesRotting([[1,0,0],[0,2,0],[0,0,0]]) == -1