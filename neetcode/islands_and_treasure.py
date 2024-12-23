"""
https://neetcode.io/problems/islands-and-treasure
https://leetcode.com/problems/walls-and-gates/description/
"""

from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead
        """
        rows = len(rooms)
        cols = len(rooms[0])

        # find gates
        nodes = []
        for i in range(rows):
            for j in range(cols):
                if rooms[i][j] == 0:
                    nodes.append([i,j])
        
        count = 0
        while len(nodes)>0:
            new_nodes = []
            for node in nodes:
                i,j = node
                curr_val = rooms[i][j]
                if i>0 and rooms[i-1][j]==2**31 - 1: # top
                    rooms[i-1][j] = curr_val + 1
                    new_nodes.append([i-1,j])
                if i<(rows-1) and rooms[i+1][j]==2**31 - 1: # bottom
                    rooms[i+1][j] = curr_val + 1 
                    new_nodes.append([i+1,j])
                if j>0 and rooms[i][j-1]==2**31 - 1: # left
                    rooms[i][j-1] = curr_val + 1
                    new_nodes.append([i,j-1])
                if j<(cols-1) and rooms[i][j+1]==2**31 - 1: # right
                    rooms[i][j+1] = curr_val + 1
                    new_nodes.append([i,j+1])
            nodes = new_nodes

solution = Solution()



rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
solution.wallsAndGates(rooms)
assert rooms == [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

rooms = [[-1]]
solution.wallsAndGates(rooms)
assert rooms == [[-1]]