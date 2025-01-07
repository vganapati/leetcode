from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-weight for weight in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            w1 = -heapq.heappop(stones)
            w2 = -heapq.heappop(stones)

            if w1 == w2:
                pass
            else:
                new_w = w1 - w2
                heapq.heappush(stones, -new_w)
        
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0

solution = Solution()

stones = [2,3,6,2,4]
assert solution.lastStoneWeight(stones) == 1

stones = [1,2]
assert solution.lastStoneWeight(stones) == 1
