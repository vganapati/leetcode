"""
https://neetcode.io/problems/surrounded-regions
"""

from typing import List
import copy

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        inverted_board = copy.deepcopy(board)
        num_rows = len(board)
        num_cols = len(board[0])

        def dfs(i,j):
            nodes = [(i,j)]
            inverted_board[i][j] = "X"
            while len(nodes)>0:
                (i,j) = nodes.pop()
                # above
                if i>0:
                    if inverted_board[i-1][j] == "O":
                        nodes.append((i-1,j))
                        inverted_board[i-1][j] = "X"
                # below
                if i<num_rows-1:
                    if inverted_board[i+1][j] == "O":
                        nodes.append((i+1, j))
                        inverted_board[i+1][j] = "X"
                
                #left
                if j>0:
                    if inverted_board[i][j-1] == "O":
                        nodes.append((i, j-1))
                        inverted_board[i][j-1] = "X"
                
                # right
                if j<num_cols-1:
                    if inverted_board[i][j+1] == "O":
                        nodes.append((i, j+1))
                        inverted_board[i][j+1] = "X"


        # go around edges
        j = 0
        for i in range(num_rows):
            if inverted_board[i][j] == "O":
                dfs(i, j)

        j = num_cols - 1
        for i in range(num_rows):
            if inverted_board[i][j] == "O":
                dfs(i, j)

        i = 0
        for j in range(num_cols):
            if inverted_board[i][j] == "O":
                dfs(i, j)
        
        i = num_rows-1
        for j in range(num_cols):
            if inverted_board[i][j] == "O":
                dfs(i, j)
        
        for i in range(num_rows):
            for j in range(num_cols):
                if inverted_board[i][j] == "O" and board[i][j] == "O":
                    board[i][j] = "X"
        
        return board
        

solution = Solution()

board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]

output = [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","O"]
]

assert solution.solve(board) == output