from typing import List

class Solution:    
    def combine(self, n: int, k: int) -> List[List[int]]:

        def combine_0(full_list, k):
            if k==1:
                return [[i] for i in full_list]
            
            all_combos = []
            for ind, i in enumerate(full_list):
                combos = combine_0(full_list[ind+1:],k-1)
                # print(combos)
                all_combos += [combo + [i] for combo in combos]
                # print(all_combos)
            # print(all_combos)
            return all_combos
        
        full_list = list(range(1,n+1))
        return combine_0(full_list, k)

    
solution = Solution()
n = 4; k = 2
print(solution.combine(n,k)) #[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]


n = 1; k = 1
print(solution.combine(n,k)) #[[1]]