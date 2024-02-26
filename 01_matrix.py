'''Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.'''

def update_matrix(mat):
    queue = []
    # Traverse matrix and add positions of zeros to the queue and mark all others for processing
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if mat[r][c] == 0:
                queue.append((r, c))
            else:
                mat[r][c] = -1
    while len(queue):
        row, col = queue.pop(0)
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        # Check all neighbors for cells that have not been processed
        for nrow, ncol in neighbors:
            if 0 <= nrow < len(mat) and 0 <= ncol < len(mat[0]) and mat[nrow][ncol] == -1:
                # Change these unprocessed cells to be one greater than the current cell
                mat[nrow][ncol] = mat[row][col] + 1
                # Add them to the queue to help process their neighbors
                queue.append((nrow, ncol))
    return mat

# TESTS

print(update_matrix([[0,0,0],[0,1,0],[1,1,1]]))
# >>[[0,0,0],[0,1,0],[1,2,1]]

print(update_matrix([[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]))
# >>[[0,0,0],[0,1,0],[1,2,1]]