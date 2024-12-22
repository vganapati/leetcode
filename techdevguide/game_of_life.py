"""
https://leetcode.com/problems/game-of-life/
"""

from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead
        """
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                live_neighbors = 0
                for ii in range(-1,2):
                    for jj in range(-1,2):
                        if not (ii == 0 and jj == 0):
                            neighbor = board[i+ii][j+jj] if (i+ii)>=0 and (i+ii)<rows and (j+jj)>=0 and (j+jj)<cols else 0
                            if neighbor == 1 or neighbor == -1:
                                live_neighbors += 1
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1
                else:
                    if live_neighbors == 3:
                        board[i][j] = 2
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1


solution = Solution()

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
solution.gameOfLife(board)
assert board == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

board = [[1,1],[1,0]]
solution.gameOfLife(board)
assert board == [[1,1],[1,1]]