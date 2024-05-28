def generate(numRows):
    rows_list = [[1]]

    for ind_i in range(1,numRows):
        current_row = []
        for ind_j in range(-1, len(rows_list[-1])):
            if ind_j == -1:
                current_row.append(rows_list[-1][0])
            elif ind_j == len(rows_list[-1])-1:
                current_row.append(rows_list[-1][-1])
            else:
                current_row.append(rows_list[-1][ind_j]+rows_list[-1][ind_j+1])
        rows_list.append(current_row)
    return rows_list

def test_0():
    numRows = 5
    assert generate(numRows) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

if __name__ == '__main__':
    test_0()