"""
https://leetcode.com/problems/merge-intervals/description/
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        

        i = 1
        while i<len(intervals):
            prev = intervals[i-1]
            curr = intervals[i]

            if curr[0] <= prev[1] or prev[0] == curr[0]:
                # merge
                new = [prev[0], max(curr[1], prev[1])]
                intervals.insert(i+1, new)
                intervals.pop(i)
                intervals.pop(i-1)
            else:
                i += 1
        return intervals


solution = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]
assert solution.merge(intervals) == [[1,6],[8,10],[15,18]]


intervals = [[1,4],[4,5]]
assert solution.merge(intervals) == [[1,5]]
