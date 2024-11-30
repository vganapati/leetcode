from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float("inf")]*n 

        cost[src] = 0
        temp = cost.copy()

        for i in range(k+1):
            for node_src, node_dst, price in flights:
                if cost[node_src] != float("inf"):
                    temp[node_dst] = min(cost[node_src] + price, cost[node_dst], temp[node_dst])
            cost = temp.copy()
        if cost[dst] != float("inf"):
            return cost[dst]
        else:
            return -1
        
solution = Solution()

n = 4; flights = [[0,1,200],[1,2,100],[1,3,300],[2,3,100]]; src = 0; dst = 3; k = 1
assert solution.findCheapestPrice(n, flights, src, dst, k) == 500

n = 3; flights = [[1,0,100],[1,2,200],[0,2,100]]; src = 1; dst = 2; k = 1
assert solution.findCheapestPrice(n, flights, src, dst, k) == 200

