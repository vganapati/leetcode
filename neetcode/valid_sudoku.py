"""
https://neetcode.io/problems/valid-sudoku
"""

from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        box_size = 3
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]
                if val == ".":
                    continue
                box_id = (i//box_size, j//box_size)
                if (val in boxes[box_id]) or (val in rows[i]) or (val in cols[j]):
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_id].add(val)
        return True


solution = Solution()

board = \
[[".",".","4",".",".",".","6","3","."],
 [".",".",".",".",".",".",".",".","."],
 ["5",".",".",".",".",".",".","9","."],
 [".",".",".","5","6",".",".",".","."],
 ["4",".","3",".",".",".",".",".","1"],
 [".",".",".","7",".",".",".",".","."],
 [".",".",".","5",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."],
 [".",".",".",".",".",".",".",".","."]]
assert solution.isValidSudoku(board) == False

board = \
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
assert solution.isValidSudoku(board) == True

board = \
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
assert solution.isValidSudoku(board) == False