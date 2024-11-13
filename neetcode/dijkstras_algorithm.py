"""
https://neetcode.io/problems/dijkstra
"""

from typing import List, Dict
from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(lambda: defaultdict(int))

        for edge in edges:
            s, d, w = edge
            adj[s][d] = w
        
        shortest = {}
        queue = [[0, src]]

        while queue:
            weight_0, node_0 = heapq.heappop(queue)
            # check the node_0 has not been visited
            if node_0 not in shortest:
                for child, weight_1 in adj[node_0].items():
                    heapq.heappush(queue, [weight_0 + weight_1, child])
                shortest[node_0] = weight_0
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest
                


if __name__ == '__main__':
    solution = Solution()

    n = 5
    edges = [[0,1,10], [0,2,3], [1,3,2], [2,1,4], [2,3,8], [2,4,2], [3,4,5]]
    src = 0
    print(solution.shortestPath(n, edges, src)) # {{0:0}, {1:7}, {2:3}, {3:9}, {4:5}}
