"""
https://neetcode.io/problems/minimum-interval-including-query
"""

from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(reverse=True)
        minHeap = []
        output = {}

        for q in sorted(queries):
            output[q] = -1
            while intervals:
                if intervals[-1][0] <= q:
                    interval = intervals.pop()
                    interval_left, interval_right = interval
                    interval_size = interval_right - interval_left + 1
                    heapq.heappush(minHeap, [interval_size, interval_right])
                else:
                    break
            while minHeap:
                
                if minHeap[0][1] >= q: # check right value of minHeap
                    output[q] = minHeap[0][0]
                    break
                else:
                    heapq.heappop(minHeap) # we have gone past the right value and the interval is no longer useful, so we remove int
        return [output[q] for q in queries]


solution = Solution()
intervals = [[1,3],[2,3],[3,7],[6,6]]; queries = [2,3,1,7,6,8]
assert solution.minInterval(intervals, queries) == [2,2,3,5,1,-1]
assert solution.minInterval([[0,10]], [0,0,10,10]) == [11,11,11,11]
assert solution.minInterval([[0,1]], [2]) == [-1]