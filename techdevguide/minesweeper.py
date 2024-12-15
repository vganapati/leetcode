from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def updateBoard_0(click):
            square = board[click[0]][click[1]]
            rows = len(board)
            cols = len(board[0])
            if square == "M":
                board[click[0]][click[1]] = "X"
                return board
            if square == "E":
                above = board[click[0]-1][click[1]]=="M" if click[0] >= 1 else False
                above_left = board[click[0]-1][click[1]-1]=="M" if (click[0] >= 1 and click[1] >= 1) else False
                above_right = board[click[0]-1][click[1]+1]=="M" if (click[0] >= 1 and (click[1] + 1) < cols) else False
                left = board[click[0]][click[1]-1]=="M" if click[1] >= 1 else False
                right = board[click[0]][click[1]+1]=="M" if (click[1]+1) < cols else False
                below = board[click[0]+1][click[1]]=="M" if (click[0] + 1) < rows else False
                below_left = board[click[0]+1][click[1]-1]=="M" if ((click[0] + 1) < rows and click[1] >= 1) else False
                below_right = board[click[0]+1][click[1]+1]=="M" if ((click[0] + 1) < rows and (click[1] + 1) < cols) else False
                mines = above + above_left + above_right + right + left + below + below_left + below_right

                if mines > 0:
                    board[click[0]][click[1]] = str(mines)
                else:
                    board[click[0]][click[1]] = "B"
                    if click[0] >= 1 and board[click[0]-1][click[1]]=="E":
                        updateBoard_0([click[0]-1,click[1]]) 
                    if (click[0] >= 1 and click[1] >= 1) and board[click[0]-1][click[1]-1]=="E":
                        updateBoard_0([click[0]-1,click[1]-1])
                    if (click[0] >= 1 and (click[1] + 1) < cols) and board[click[0]-1][click[1]+1]=="E":
                        updateBoard_0([click[0]-1,click[1]+1])
                    if click[1] >= 1 and board[click[0]][click[1]-1]=="E":
                        updateBoard_0([click[0],click[1]-1])
                    if (click[1]+1) < cols and board[click[0]][click[1]+1]=="E":
                        updateBoard_0([click[0],click[1]+1])
                    if (click[0] + 1) < rows and board[click[0]+1][click[1]]=="E":
                        updateBoard_0([click[0]+1,click[1]])
                    if ((click[0] + 1) < rows and click[1] >= 1) and board[click[0]+1][click[1]-1]=="E":
                        updateBoard_0([click[0]+1,click[1]-1])
                    if ((click[0] + 1) < rows and (click[1] + 1) < cols) and board[click[0]+1][click[1]+1]=="E":
                        updateBoard_0([click[0]+1,click[1]+1])

        updateBoard_0(click)
        return board

solution = Solution()
board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]
output = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
assert solution.updateBoard(board,click) == output

board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
click = [1,2]
output = [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
assert solution.updateBoard(board,click) == output
