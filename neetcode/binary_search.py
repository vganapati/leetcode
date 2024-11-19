from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pointer_0 = 0
        pointer_1 = len(nums)-1

        while pointer_1>=pointer_0:
            midpoint = (pointer_1 + pointer_0)//2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint]>target:
                pointer_1 = midpoint-1
            else: # nums[midpoint] < target
                pointer_0 = midpoint+1
        return -1



    def search_recursive(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        else:    
            midpoint = len(nums)//2

            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                return self.search(nums[:midpoint], target)
            else:
                val = self.search(nums[midpoint:], target)
                if val == -1:
                    return val
                else:
                    return val + midpoint

if __name__ == "__main__":
    solution = Solution()

    nums = [-1,0,2,4,6,8]
    target = 4
    assert solution.search(nums, target) == 3

    nums=[-1,0,3,5,9,12]
    target=13
    assert solution.search(nums, target) == -1

    nums=[-1,0,3,5,9,12]
    target=9
    assert solution.search(nums, target) == 4

    nums = [-1,0,2,4,6,8]
    target = 3
    assert solution.search(nums, target) == -1

