from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        evens = 0
        odds = 0
        for p in position:
            if p%2 == 0:
                evens += 1
            else:
                odds += 1
        return min(evens, odds)

solution = Solution()
position = [1,2,3]
assert solution.minCostToMoveChips(position) == 1

position = [2,2,2,3,3]
assert solution.minCostToMoveChips(position) == 2

position = [1,1000000000]
assert solution.minCostToMoveChips(position) == 1