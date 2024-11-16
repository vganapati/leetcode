"""
https://leetcode.com/problems/number-of-provinces/description/
"""

from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_cities = len(isConnected)
        parents = list(range(num_cities))
        rank = [1]*num_cities
        def find(city):
            while city != parents[city]:
                parents[city] = parents[parents[city]] # path compression
                city = parents[city]
            return city
        
        def union(city_0, city_1):
            p0, p1 = find(city_0), find(city_1)
            if p0 == p1:
                return 0
            else:
                if rank[p0] >= rank[p1]:
                    parents[p1] = p0
                    rank[p0] += rank[p1]
                else:
                    parents[p0] = p1
                    rank[p1] += rank[p0]
                return 1

        provinces = num_cities
        for i in range(num_cities):
            for j in range(i+1, num_cities):
                if isConnected[i][j]:
                    provinces -= union(i, j)
        
        return provinces

solution = Solution()
assert solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2
assert solution.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3
