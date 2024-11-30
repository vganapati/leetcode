from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        num_slides = (len(nums) - k) + 1

        max_heap = [(-num,ind) for ind,num in enumerate(nums[0:k-1])]
        heapq.heapify(max_heap)

        output = []
        for i in range(num_slides):
            heapq.heappush(max_heap, (-nums[k-1+i],k-1+i))
            while max_heap[0][1] < i:
                heapq.heappop(max_heap)
            output.append(-max_heap[0][0])
        return output




solution = Solution()
nums = [1,2,1,0,4,2,6]; k = 3
assert solution.maxSlidingWindow(nums, k) == [2,2,4,4,6]
