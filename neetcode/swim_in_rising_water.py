"""
https://neetcode.io/problems/swim-in-rising-water
"""

from typing import List
import heapq

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(f"{elem:>3}" for elem in row))
    print()

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[-1]*n for _ in range(n)]
        queue = [[grid[0][0], 0,0]]

        while queue:
            height_0, x, y = heapq.heappop(queue)
            if x == n-1 and y == n-1:
                return height_0
            if visited[x][y]==-1:
                visited[x][y] = height_0
                if x+1 < n:
                    height_1 = max(grid[x+1][y], height_0)
                    heapq.heappush(queue, [height_1, x+1, y])
                if y+1 < n:
                    height_1 = max(grid[x][y+1], height_0)
                    heapq.heappush(queue, [height_1, x, y+1])
                if x-1 > -1:
                    height_1 = max(grid[x-1][y], height_0)
                    heapq.heappush(queue, [height_1, x-1, y])
                if y-1 > -1:
                    height_1 = max(grid[x][y-1], height_0)
                    heapq.heappush(queue, [height_1, x, y-1])


if __name__ == "__main__":
    solution = Solution()

    grid = [
        [0,1,2,3,4],
        [24,23,22,21,5],
        [12,13,14,15,16],
        [11,17,18,19,20],
        [10,9,8,7,6]
        ]
    assert solution.swimInWater(grid) == 16

    assert solution.swimInWater([[0,1],[2,3]]) == 3

    grid = [
        [0,1,2,10],
        [9,14,4,13],
        [12,3,8,15],
        [11,5,7,6],
    ]
    assert solution.swimInWater(grid) == 8