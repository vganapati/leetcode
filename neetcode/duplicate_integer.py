from typing import List
from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            if counter[num] > 1:
                return True
        return False


if __name__ == "__main__":

    solution = Solution()

    nums1 = [1,2,3,3]
    assert solution.hasDuplicate(nums1) == True

    nums1 = [1,2,3,4]
    assert solution.hasDuplicate(nums1) == False

    print("All test cases passed!")