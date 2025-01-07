from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        min_cost = [0]*(len(cost)+2)

        for i in range(len(cost)-1, -1, -1):
            min_cost[i] = cost[i] + min(min_cost[i+1], min_cost[i+2])
        
        return min(min_cost[0], min_cost[1])

solution = Solution()
cost = [1,2,3]
assert solution.minCostClimbingStairs(cost) == 2

cost = [1,2,1,2,1,1,1]
assert solution.minCostClimbingStairs(cost) == 4