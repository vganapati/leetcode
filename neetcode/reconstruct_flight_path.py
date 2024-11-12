from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse=True)
        
        for ticket in tickets:
            adj[ticket[0]].append(ticket[1])
        
        itinerary = []
        def dfs(start):
            while adj[start]:
                dest = adj[start].pop()
                dfs(dest)
            itinerary.append(start)
        dfs("JFK")
        return itinerary[::-1]

if __name__ == '__main__':
    solution = Solution()
    assert solution.findItinerary([["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]) == ["JFK","BUF","HOU","SEA"]
    assert solution.findItinerary([["HOU","JFK"],["SEA","JFK"],["JFK","SEA"],["JFK","HOU"]]) == ["JFK","HOU","JFK","SEA","JFK"]