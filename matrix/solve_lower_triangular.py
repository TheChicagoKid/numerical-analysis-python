def solve_lower(A, b):
    """
    Solves the equation Ax = b where x and b are vectors (python lists) and A
    is a lower triangular matrix (python list of lists)
    Args:
        A: Lower triangular matrix (Ax = b)
        b: Right hand side vector (Ax = b)
    Returns:
        The vector x that we are solving for (Ax = b)
    """
    n = len(b)
    x = [0 for _ in range(n)]

    for i in range(n):
        x[i] = b[i]
        for j in range(i):
            print(j)
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


A = [[1, 0, 0], [5, 1, 0], [10, 2, 1]]
b = [7, 4, 6]
print(solve_lower(A, b))
