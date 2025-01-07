from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)

        for num in nums:
            hm[num] += 1
        
        min_heap = [(-val, key) for key, val in hm.items()]
        heapq.heapify(min_heap)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(min_heap)[1])
        
        return result
        
solution = Solution()

nums = [1,2,2,3,3,3]; k = 2
assert solution.topKFrequent(nums, k) == [2,3] or solution.topKFrequent(nums, k) == [3,2]


nums = [7,7]; k = 1
assert solution.topKFrequent(nums, k) == [7]
