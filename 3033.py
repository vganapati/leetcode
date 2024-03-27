import numpy as np

def modifiedMatrix(matrix):
    matrix = np.array(matrix)
    max_vals = np.repeat(np.max(matrix, axis=0)[None,:], matrix.shape[0],axis=0)
    matrix[matrix==-1] = max_vals[matrix==-1]
    return matrix.tolist()

def test_0():
    matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
    assert modifiedMatrix(matrix) == [[1,2,9],[4,8,6],[7,8,9]]

def test_1():
    matrix = [[3,-1],[5,2]]
    assert modifiedMatrix(matrix) == [[3,2],[5,2]]

if __name__ == '__main__':
    test_0()
    test_1()