import math


def cholesky(matrix):
    """
    Perform the Cholesky decomposition

    Args:
        matrix: The actual square matrix we are decomposing
    Returns:
        The lower triangular matrix L of the equation A = L*L_T
    """

    # Assuming this is a square matrix, n should equal the number of columns and rows
    n = len(matrix)

    # Calculate values for first column of L
    l = [[0] * n for _ in range(n)]
    l[0][0] = math.sqrt(matrix[0][0])
    for j in range(1, n):
        l[j][0] = matrix[j][0] / l[0][0]

    # Main loop to calculate all entries except Lnn
    for i in range(1, n - 1):
        total = 0
        for k in range(i):
            total += (l[i][k]) ** 2
        l[i][i] = math.sqrt(matrix[i][i] - total)

        for j in range(i + 1, n):
            total = 0
            for k in range(i):
                total += l[j][k] * l[i][k]
            l[j][i] = (matrix[j][i] - total) / l[i][i]

    # Calculate final Lnn entry
    total = 0
    for k in range(n - 1):
        total += (l[n - 1][k]) ** 2
    l[n - 1][n - 1] = math.sqrt(matrix[n - 1][n - 1] - total)

    return l
