"""
https://leetcode.com/problems/pacific-atlantic-water-flow/description/
"""

from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific = [[0]*cols for _ in range(rows)]
        atlantic = [[0]*cols for _ in range(rows)]

        pacific_nodes = []
        atlantic_nodes = []

        for i in range(rows):
            pacific[i][0] = 1
            pacific_nodes.append((i,0))

            atlantic[i][cols-1] = 1
            atlantic_nodes.append((i, cols-1))

        for j in range(cols):
            pacific[0][j] = 1
            pacific_nodes.append((0,j))

            atlantic[rows-1][j] = 1
            atlantic_nodes.append((rows-1, j))

        def dfs(pacific_nodes, pacific):    
            while len(pacific_nodes)>0:
                (i,j) = pacific_nodes.pop()
                curr_height = heights[i][j]
                if i>0:
                    # north
                    if pacific[i-1][j] == 0 and heights[i-1][j] >= curr_height:
                        pacific_nodes.append((i-1, j))
                        pacific[i-1][j] = 1
                if (j+1)<cols:
                    # east
                    if pacific[i][j+1] == 0 and heights[i][j+1] >= curr_height:
                        pacific_nodes.append((i, j+1))
                        pacific[i][j+1] = 1
                if (i+1)<rows:
                    # south
                    if pacific[i+1][j] == 0 and heights[i+1][j] >= curr_height:
                        pacific_nodes.append((i+1, j))
                        pacific[i+1][j] = 1
                if j>0:
                    # west
                    if pacific[i][j-1] == 0 and heights[i][j-1] >= curr_height:
                        pacific_nodes.append((i, j-1))
                        pacific[i][j-1] = 1

        dfs(pacific_nodes, pacific)
        dfs(atlantic_nodes, atlantic)

        output = []
        for i in range(rows):
            for j in range(cols):
                if pacific[i][j] and atlantic[i][j]:
                    output.append([i,j])

        return output
        


solution = Solution()

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(solution.pacificAtlantic(heights)) # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

heights = [[1]]
assert solution.pacificAtlantic(heights) == [[0,0]]