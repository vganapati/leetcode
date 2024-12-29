from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        biggestSquares = [[0]*cols for _ in range(rows)]

        level = 1
        while level <= max(rows, cols):
            for i in range(rows-1, rows-level, -1):
                if i>-1 and (cols-level)>-1 and matrix[i][cols-level] == '1':
                    below=biggestSquares[i+1][cols-level] if (i+1)<rows else 0
                    diag= biggestSquares[i+1][cols-level+1] if ((i+1)<rows and (cols-level+1)<cols) else 0
                    right = biggestSquares[i][cols-level+1] if (cols-level+1)<cols else 0
                    biggestSquares[i][cols-level] = min(below,diag,right)+1
            for j in range(cols-1, cols-level, -1):
                if (rows-level) > -1 and j>-1 and matrix[rows-level][j] =='1':
                    right=biggestSquares[rows-level][j+1] if (j+1)<cols else 0
                    diag= biggestSquares[rows-level+1][j+1] if ((j+1)<cols and (rows-level+1)<rows) else 0
                    below = biggestSquares[rows-level+1][j] if (rows-level+1)<rows else 0
                    biggestSquares[rows-level][j] = min(below,diag,right)+1
            if (rows-level) > -1 and (cols-level)>-1 and matrix[rows-level][cols-level] == '1':
                below=biggestSquares[rows-level+1][cols-level] if (rows-level+1)<rows else 0
                diag= biggestSquares[ rows-level+1][cols-level+1] if ((cols-level+1)<cols and (rows-level+1)<rows) else 0
                right = biggestSquares[rows-level][cols-level+1] if (cols-level+1)<cols else 0
                biggestSquares[rows-level][cols-level] = min(below,diag,right)+1             
            level += 1  

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                max_area = max(max_area,(biggestSquares[i][j])**2)
        
        return max_area


    def maximalSquare_0(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        min_dim = min(rows, cols)

        def getArea(i,j):
            level = 1
            while (i+level)<rows and (j+level)<cols:
                for ii in range(level+1):
                    if matrix[i+ii][j+level] == '0':
                        return level
                for jj in range(level+1):
                    if matrix[i+level][j+jj] == '0':
                        return level
                level += 1
            
            return level
            
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if (min(rows - i, cols-j))**2 <= max_area:
                    pass
                if matrix[i][j] == '1':
                    level = getArea(i,j)
                    max_area = max(max_area, level**2)
        return max_area

solution = Solution()

matrix = [["0","0","0","1"],
          ["1","1","0","1"],
          ["1","1","1","1"],
          ["0","1","1","1"],
          ["0","1","1","1"]]
assert solution.maximalSquare(matrix)==9

matrix = [["1","1","1","1","0"],
          ["1","1","1","1","0"],
          ["1","1","1","1","1"],
          ["1","1","1","1","1"],
          ["0","0","1","1","1"]]
assert solution.maximalSquare(matrix)==16

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
assert solution.maximalSquare(matrix)==4

matrix = [["0","1"],["1","0"]]
assert solution.maximalSquare(matrix)==1

matrix = [["0"]]
assert solution.maximalSquare(matrix)==0