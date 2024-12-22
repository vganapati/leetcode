"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/
"""

from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent_rank = [[ind,1] for ind in range(len(stones))]

        def find(ind):
            while parent_rank[ind][0] != ind:
                parent_rank[ind] = parent_rank[parent_rank[ind][0]]
                ind = parent_rank[ind][0]
            return ind
        
        def join(ind_0, ind_1):
            p0, r0 = parent_rank[find(ind_0)]
            p1, r1 = parent_rank[find(ind_1)]
            if p0 == p1:
                return 0
            else:
                if r0 >= r1:
                    parent_rank[p0][1] += r1
                    parent_rank[p1] = parent_rank[p0]
                else:
                    parent_rank[p1][1] += r0
                    parent_rank[p0] = parent_rank[p1]       
                return 1             
                             
        num_merges = 0
        for i in range(len(stones)):
            row_i, col_i = stones[i]
            for j in range(i+1,len(stones)):
                row_j, col_j = stones[j]
                if row_j == row_i or col_j == col_i:
                    merged = join(i,j)
                    num_merges += merged
        return num_merges

solution = Solution()

stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
assert solution.removeStones(stones) == 5

stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
assert solution.removeStones(stones) == 3

stones = [[0,0]]
assert solution.removeStones(stones) == 0