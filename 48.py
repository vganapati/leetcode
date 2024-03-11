def rotate(matrix):
    for row in range(len(matrix)):
        for column in range(row+1, len(matrix[0])):
            matrix[row][column], matrix[column][row] = matrix[column][row], matrix[row][column]

    # flip on vertical
    for row in range(len(matrix)):
        for column in range(0, len(matrix[0])//2):
            matrix[row][column], matrix[row][len(matrix[0])-column-1] = matrix[row][len(matrix[0])-column-1], matrix[row][column]


def test_0():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)
    assert matrix == [[7,4,1],[8,5,2],[9,6,3]]

if __name__ == "__main__":
    test_0()