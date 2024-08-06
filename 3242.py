from typing import List

class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid

    def adjacentSum(self, value: int) -> int:
        flag = False
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] == value:
                    flag = True
                    break
            if flag:
                break
        val = 0
        if i-1 >= 0:
            val += self.grid[i-1][j]
        if i+1 < len(self.grid):
            val += self.grid[i+1][j]
        if j-1 >= 0:
            val += self.grid[i][j-1]
        if j+1 < len(self.grid):
            val += self.grid[i][j+1]
        return val
    def diagonalSum(self, value: int) -> int:
        flag = False
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] == value:
                    flag = True
                    break
            if flag:
                break

        val = 0
        if i-1 >= 0 and j-1 >=0:
            val += self.grid[i-1][j-1]
        if i+1 < len(self.grid) and j+1 < len(self.grid):
            val += self.grid[i+1][j+1]
        
        if i+1 < len(self.grid) and j-1 >=0:
            val += self.grid[i+1][j-1]
        if i-1 >= 0 and j+1 < len(self.grid):
            val += self.grid[i-1][j+1]
        return val

obj = neighborSum([[0,1,2],[3,4,5],[6,7,8]])
print(obj.adjacentSum(1)==6)
print(obj.diagonalSum(4)==16) 