from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        pointer_0 = 0
        pointer_1 = 1

        if k==1:
            return True
    
        while pointer_1 < len(nums) - k:
            if nums[pointer_1] > nums[pointer_1-1]:
                if (pointer_1-pointer_0+1) == k:
                    flag = True
                    for i in range(pointer_1+1,pointer_1+k):
                        if nums[i] < nums[i+1]:
                            pass
                        else:
                            flag = False
                            break
                    if flag:
                        return True
                    pointer_0 +=1
                    pointer_1 +=1
                else:
                    pointer_1 += 1
            else:
                pointer_0 = pointer_1
                pointer_1 += 1
        return False

if __name__ == "__main__":
    solution = Solution()
    assert solution.hasIncreasingSubarrays([-15,3,16,0], 2) == False
    assert solution.hasIncreasingSubarrays([-9,9,12,3,6],2) == True
    assert solution.hasIncreasingSubarrays([-2,-1,3,-2,-16,-2], 3) == False
    assert solution.hasIncreasingSubarrays([-15,19],1) == True
    assert solution.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3) == True
    assert solution.hasIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7], 5) == False

            