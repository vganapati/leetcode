from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        is_even = (len(nums1) + len(nums2))%2 == 0
        partition_size = (len(nums1) + len(nums2))//2
        if len(nums1) > len(nums2):
            small_array, large_array = nums2, nums1
        else:
            small_array, large_array = nums1, nums2
        

        left, right = 0, len(small_array)-1

        while True:
            middle = (left + right)//2
            middle_2 = partition_size - middle  - 1 - 1

            small_left = small_array[middle] if middle>=0 else float("-inf") # within partition
            small_right = small_array[middle+1] if (middle+1) < len(small_array) else float("inf") # outside partition
            large_left = large_array[middle_2] if middle_2 >= 0 else float("-inf")
            large_right = large_array[middle_2+1] if (middle_2+1) < len(large_array) else float("inf")

            if small_left <= large_right and large_left <= small_right:
                if is_even:
                    return (max(small_left, large_left) + min(small_right, large_right))/2
                else:
                    return min(small_right, large_right)
            elif small_left> large_right:
                right = middle - 1
            else:
                left = middle + 1
 
solution = Solution()

nums1 = [1]; nums2 = [3]
assert solution.findMedianSortedArrays(nums1, nums2) == 2.0

nums1 = [1,2]; nums2 = [3]
assert solution.findMedianSortedArrays(nums1, nums2) == 2.0

nums1 = [1,3]; nums2 = [2,4]
assert solution.findMedianSortedArrays(nums1, nums2) == 2.5

