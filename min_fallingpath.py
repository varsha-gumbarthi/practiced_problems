def minFallingPathSum(matrix):
    n = len(matrix)
    
    # Start from second last row to top
    for i in range(n - 2, -1, -1):
        for j in range(n):
            best = matrix[i + 1][j]  # directly below
            if j > 0:
                best = min(best, matrix[i + 1][j - 1])  # bottom-left
            if j < n - 1:
                best = min(best, matrix[i + 1][j + 1])  # bottom-right
            matrix[i][j] += best

    return min(matrix[0])
