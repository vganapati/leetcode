from typing import List
import heapq

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        dist_mat = []
        for ind_w, worker in enumerate(workers):
            dist_vec = []
            for ind_b, bike in enumerate(bikes):
                dist = abs(worker[0]-bike[0]) + abs(worker[1]-bike[1])
                dist_vec.append([dist, ind_w, ind_b])
            heapq.heapify(dist_vec)
            dist_mat.append(dist_vec)
        
        heapq.heapify(dist_mat)
        assigned_bikes_list = [0]*len(workers)
        assigned_bikes_set = set()
        while len(dist_mat)>0:
            dist_vec = heapq.heappop(dist_mat)
            [dist, ind_w, ind_b] = heapq.heappop(dist_vec)
            if ind_b not in assigned_bikes_set:
                assigned_bikes_list[ind_w] = ind_b
                assigned_bikes_set.add(ind_b)
            else:
                heapq.heappush(dist_mat, dist_vec)
        return assigned_bikes_list


solution = Solution()

workers = [[0,0],[1,1],[2,0]]; bikes = [[1,0],[2,2],[2,1]]
assert solution.assignBikes(workers, bikes) == [0,2,1]

workers = [[0,0],[2,1]]; bikes = [[1,2],[3,3]]
assert solution.assignBikes(workers, bikes) == [1,0]

