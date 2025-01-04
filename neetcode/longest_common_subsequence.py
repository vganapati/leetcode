"""
https://neetcode.io/problems/longest-common-subsequence
https://leetcode.com/problems/longest-common-subsequence/description/
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + memo[i+1][j+1]
                else:
                    memo[i][j] = max(memo[i][j+1], memo[i+1][j])
        return memo[0][0]

solution = Solution()

text1 = "abcde"; text2 = "ace" 
assert solution.longestCommonSubsequence(text1, text2) == 3  

text1 = "abc"; text2 = "abc"
assert solution.longestCommonSubsequence(text1, text2) == 3

text1 = "abc"; text2 = "def"
assert solution.longestCommonSubsequence(text1, text2) == 0
