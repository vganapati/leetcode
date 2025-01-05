class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        memo = [[0]*(n+1) for _ in range(m+1)]

        count = 0
        for i in range(m, -1, -1):
            memo[i][n] = count
            count += 1
        
        count = 0
        for j in range(n, -1, -1):
            memo[m][j] = count
            count += 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]: # keep
                    memo[i][j] = memo[i+1][j+1]
                else:
                    options = []
                    options.append(memo[i][j+1]+1) # insert
                    options.append(memo[i+1][j]+1) # delete
                    options.append(memo[i+1][j+1]+1) # replace
                    memo[i][j] = min(options)
        return memo[0][0]

solution = Solution()
word1 = "horse"; word2 = "ros"
assert solution.minDistance(word1, word2) == 3

solution = Solution()
word1 = "intention"; word2 = "execution"
assert solution.minDistance(word1, word2) == 5