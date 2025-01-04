"""
https://leetcode.com/problems/unique-paths/description/
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0]*n for _ in range(m)]

        for i in range(m):
            memo[i][n-1] = 1

        for j in range(n):
            memo[m-1][j] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                memo[i][j] = memo[i+1][j] + memo[i][j+1]
        
        return memo[0][0]

                
solution = Solution()
m = 3; n = 7
assert solution.uniquePaths(m, n) == 28