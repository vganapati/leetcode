class Solution:
    def climbStairs(self, n: int) -> int:
        num_ways = [0]*(n+2)
        num_ways[n] = 1

        for i in range(n-1, -1, -1):
            num_ways[i] = num_ways[i+1] + num_ways[i+2]
        
        return num_ways[0]
    
solution = Solution()

assert solution.climbStairs(2) == 2
assert solution.climbStairs(3) == 3