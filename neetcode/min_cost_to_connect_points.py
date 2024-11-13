from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}
        for i in range(len(points)):
            x_0, y_0 = points[i]
            for j in range(i+1,len(points)):
                x_1, y_1 = points[j]
                dist = abs(x_0 - x_1) + abs(y_0 - y_1)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        # Prim's algorithm
        minHeap = [[0,0]] # [dist, point]
        visited = set()
        cost = 0

        while len(visited) < len(points):
            dist, point = heapq.heappop(minHeap)
            if point in visited:
                pass
            else:
                cost += dist
                visited.add(point)
                for neighborDist, neighborPoint in adj[point]:
                    heapq.heappush(minHeap, [neighborDist, neighborPoint])
        return cost

solution = Solution()
assert solution.minCostConnectPoints([[0,0],[2,2],[3,3],[2,4],[4,2]]) == 10
assert solution.minCostConnectPoints([[0,0]]) == 0
assert solution.minCostConnectPoints([[0,0], [0,10]]) == 10