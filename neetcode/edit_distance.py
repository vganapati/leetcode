"""
https://leetcode.com/problems/edit-distance/description/
https://neetcode.io/problems/edit-distance
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def minDistance_0(word1, word2):
            if (word1, word2) in memo:
                return memo[(word1, word2)]
            
            if word1 == word2:
                return 0
            
            if len(word1) == 0:
                return len(word2)
            
            if len(word2) == 0:
                return len(word1)

            if word1[0] == word2[0]: # keep
                memo[(word1, word2)] = minDistance_0(word1[1:], word2[1:])
                return memo[(word1, word2)]
            
            options = []

            # replace
            options.append(minDistance_0(word1[1:], word2[1:])+1)
            
            # insert
            options.append(minDistance_0(word1, word2[1:])+1)

            # delete
            options.append(minDistance_0(word1[1:], word2)+1)

            memo[(word1, word2)] = min(options)

            return memo[(word1, word2)]
        return minDistance_0(word1, word2)

solution = Solution()
word1 = "horse"; word2 = "ros"
assert solution.minDistance(word1, word2) == 3

solution = Solution()
word1 = "intention"; word2 = "execution"
assert solution.minDistance(word1, word2) == 5