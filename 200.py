def findNeighbors(grid, grid_rows, grid_cols, i, j):
    neighbors = []

    # up
    if i-1>=0:
        if grid[i-1][j] == "1":
            neighbors.append([i-1,j])

    # down
    if i+1 < grid_rows:
        if grid[i+1][j] == "1":
            neighbors.append([i+1,j])

    # left
    if j-1>=0:
        if grid[i][j-1] == "1":
            neighbors.append([i,j-1])

    # right
    if j+1 < grid_cols:
        if grid[i][j+1] == "1":
            neighbors.append([i,j+1])
    return neighbors

def deleteIsland(grid, grid_rows, grid_cols, i, j):
    current_points = [[i,j]]
    while len(current_points)>0:
        # take last point off stack
        point = current_points.pop()
        neighbors = findNeighbors(grid, grid_rows, grid_cols, point[0], point[1])
        grid[point[0]][point[1]] = "0"
        current_points += neighbors
    return grid


def numIslands(grid):
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    num_islands = 0
    for i in range(grid_rows):
        for j in range(grid_cols):
            if grid[i][j] == "1":
                grid = deleteIsland(grid, grid_rows, grid_cols, i, j)
                num_islands += 1
    return num_islands
    

def test_0():
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert numIslands(grid) == 1

def test_1():
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert numIslands(grid) == 3

if __name__ == "__main__":
    test_0()
    test_1()