from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [[(i**2 + j**2)**0.5, [i,j]] for [i,j] in points]
        heapq.heapify(dists)
        return [heapq.heappop(dists)[1] for i in range(k)]

solution = Solution()

points = [[0,2],[2,2]]; k = 1
assert solution.kClosest(points, k) == [[0,2]]


points = [[0,2],[2,0],[2,2]]; k = 2
assert solution.kClosest(points, k) == [[0,2],[2,0]]
