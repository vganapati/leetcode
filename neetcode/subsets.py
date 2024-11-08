from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        else:
            subsets_1 = self.subsets(nums[1:])
            return subsets_1 + [[nums[0]]+s for s in subsets_1]
                
    def subsets_iterative(self, nums: List[int]) -> List[List[int]]:
        subsets_vec = [[]]
        for num in nums:
            subsets_vec += [s + [num] for s in subsets_vec]
        return subsets_vec

if __name__ == "__main__":
    solution = Solution()
    solution.subsets([1,2,3]) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    print(solution.subsets_iterative([1,2,3]))