from typing import List
import heapq

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        city_graph = {}
        for city in range(n-1):
            city_graph[city] = [city + 1]

        shortest_paths = [n-1]*len(queries)
        for ind, query in enumerate(queries):
            if query[1] not in city_graph[query[0]]: # do not repeat for duplicate queries
                city_graph[query[0]].append(query[1])
                shortest_paths[ind] = self.shortest_path(n, city_graph)
            else:
                if ind == 0:
                    pass
                else:
                    shortest_paths[ind] = shortest_paths[ind-1]
        return shortest_paths

    def shortest_path(self, n, city_graph):
        priority_queue = [(0,0)]
        dist_vec = [0] + [float('inf')]*(n-1)
        unvisited_nodes = [True]*n

        while len(priority_queue)>0:
            current_dist, current_node = heapq.heappop(priority_queue)
            unvisited_nodes[current_node] = False
            if current_node == n-1:
                return int(current_dist)
            neighbors = city_graph[current_node]
            for neighbor in neighbors:
                if unvisited_nodes[neighbor]:
                    dist_vec[neighbor] = min(current_dist + 1, dist_vec[neighbor])
                    heapq.heappush(priority_queue, (dist_vec[neighbor], neighbor))
                    
                
print(Solution().shortestDistanceAfterQueries(5, [[2,4],[0,2],[0,4]]) == [3,2,1])
print(Solution().shortestDistanceAfterQueries(4, [[0,3],[0,2]]) == [1,1])
print(Solution().shortestDistanceAfterQueries(6, [[1,4],[0,2]]) == [3,3]) 

