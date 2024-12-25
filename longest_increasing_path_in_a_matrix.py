"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
"""

from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        longest_paths = [[0]*cols for _ in range(rows)]

        def find_path(i,j):
            curr = matrix[i][j]
            if longest_paths[i][j] == 0:
                possible_paths = [1]
                if i>0 and matrix[i-1][j]>curr:
                    possible_paths.append(1+find_path(i-1,j))
                if i<(rows-1) and matrix[i+1][j]>curr:
                    possible_paths.append(1+find_path(i+1,j))
                if j>0 and matrix[i][j-1]>curr:
                    possible_paths.append(1+find_path(i,j-1))
                if j<(cols-1) and matrix[i][j+1]>curr:
                    possible_paths.append(1+find_path(i,j+1))
                longest_path = max(possible_paths)
                longest_paths[i][j] = longest_path
                return longest_path
            else:
                return longest_paths[i][j]

        longest_path = 0
        for i in range(rows):
            for j in range(cols):
                longest_path = max(longest_path, find_path(i,j))
        return longest_path
    
solution = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
assert solution.longestIncreasingPath(matrix) == 4

matrix = [[3,4,5],[3,2,6],[2,2,1]]
assert solution.longestIncreasingPath(matrix) == 4

matrix = [[1]]
assert solution.longestIncreasingPath(matrix) == 1