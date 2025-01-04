"""
https://leetcode.com/problems/interleaving-string/description/
https://neetcode.io/problems/interleaving-string
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        rows = len(s1)
        cols = len(s2)

        memo = [[False]*(cols+1) for _ in range(rows+1)]

        memo[rows][cols] = True

        for i in range(rows):
            if s3[cols+i:] == s1[i:]:
                memo[i][cols] = True
        
        for j in range(cols):
            if s3[rows+j:] == s2[j:]:
                memo[rows][j] = True
        
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                if s3[i+j] == s1[i] and memo[i+1][j]:
                    memo[i][j] = True
                elif s3[i+j] == s2[j] and memo[i][j+1]:
                    memo[i][j] = True        
        return memo[0][0]




solution = Solution()

s1 = ""; s2 = ""; s3 = "a"
assert solution.isInterleave(s1, s2, s3) == False

s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbcbcac"
assert solution.isInterleave(s1, s2, s3) == True

s1 = "aabcc"; s2 = "dbbca"; s3 = "aadbbbaccc"
assert solution.isInterleave(s1, s2, s3) == False

s1 = ""; s2 = ""; s3 = ""
assert solution.isInterleave(s1, s2, s3) == True
