from typing import List
import numpy as np

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        city_graph = {}
        for city in range(n-1):
            city_graph[city] = [city + 1]

        dist = n-1
        shortest_paths = []
        for query in queries:
            city_graph[query[0]].append(query[1])
            dist = self.shortest_path(n, city_graph)
            shortest_paths.append(dist)
        return shortest_paths
    
    def shortest_path(self, n, city_graph):
        all_nodes = np.arange(n)
        dist_vec = [0] + [np.inf]*(n-1)
        dist_vec = np.array(dist_vec)
        unvisited_nodes = np.ones(n, dtype=bool)
        
        while sum(unvisited_nodes)>0:
            current_node = all_nodes[unvisited_nodes][np.argmin(dist_vec[unvisited_nodes])]
            unvisited_nodes[current_node] = False
            if current_node == n-1:
                return int(dist_vec[current_node])
            neighbors = city_graph[current_node]
            for neighbor in neighbors:
                if unvisited_nodes[neighbor]:
                    dist_vec[neighbor] = min(dist_vec[current_node] + 1, dist_vec[neighbor])

                
print(Solution().shortestDistanceAfterQueries(5, [[2,4],[0,2],[0,4]])) #[3,2,1]


print(Solution().shortestDistanceAfterQueries(4, [[0,3],[0,2]])) # [1,1]

print(Solution().shortestDistanceAfterQueries(6, [[1,4],[0,2]])) # [3,3]

