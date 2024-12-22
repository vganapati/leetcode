from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        pointer_0 = 0
        pointer_1 = len(arr) - 1

        while True:
            mid = (pointer_0 + pointer_1)//2
            print(pointer_0, mid, pointer_1)
            mid_val = arr[mid]
            prev = arr[mid-1] if mid>0 else -1
            after = arr[mid+1] if (mid+1)<len(arr) else -1
            if mid_val>prev and mid_val>after:
                return mid
            elif prev>mid_val:
                pointer_1 = mid-1
            else:
                pointer_0 = mid+1

solution = Solution()

arr = [3,9,8,6,4]
assert solution.peakIndexInMountainArray(arr) == 1

arr = [0,1,0]
assert solution.peakIndexInMountainArray(arr) == 1

arr = [0,2,1,0]
assert solution.peakIndexInMountainArray(arr) == 1

arr = [0,10,5,2]
assert solution.peakIndexInMountainArray(arr) == 1