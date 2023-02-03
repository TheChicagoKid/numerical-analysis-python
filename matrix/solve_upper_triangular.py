def solve_upper(A, b):
    """
    Solves the equation Ax = b where x and b are vectors (python lists) and A
    is an upper triangular matrix (python list of lists)
    Args:
        A: Upper triangular matrix (Ax = b)
        b: Right hand side vector (Ax = b)
    Returns:
        The vector x that we are solving for (Ax = b)
    """
    n = len(b)
    x = [0 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(n - 1, i, -1):
            print(j)
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


A = [[1, -5, 1], [0, 25, -6], [0, 0, 22]]
b = [7, -31, -2]

print(solve_upper(A, b))
