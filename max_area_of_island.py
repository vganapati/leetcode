"""
https://leetcode.com/problems/max-area-of-island/description/
https://neetcode.io/problems/max-area-of-island
"""
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def find_area(i,j):
            area = 1
            nodes = [(i,j)]
            grid[i][j] = 0

            while len(nodes)>0:
                i,j = nodes.pop()

                # get neighbors
                if i>0 and grid[i-1][j] == 1:
                    nodes.append((i-1,j))
                    grid[i-1][j] = 0
                    area += 1
                if i<(rows-1) and grid[i+1][j] == 1:
                    nodes.append((i+1, j))
                    grid[i+1][j] = 0
                    area += 1
                if j>0 and grid[i][j-1] == 1:
                    nodes.append((i,j-1))
                    grid[i][j-1] = 0
                    area += 1
                if j<(cols-1) and grid[i][j+1] == 1:
                    nodes.append((i, j+1))
                    grid[i][j+1] = 0
                    area += 1
            return area

        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    # find all connected 1s
                    area = find_area(i,j)
                    max_area = max(area, max_area)

        return max_area


solution = Solution()

grid = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]]
assert solution.maxAreaOfIsland(grid) == 4

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
assert solution.maxAreaOfIsland(grid) == 6

grid = [[0,0,0,0,0,0,0,0]]
assert solution.maxAreaOfIsland(grid) == 0