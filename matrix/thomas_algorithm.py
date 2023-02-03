def thomas(n, epsilon):
    """
    Perform the Thomas algorithm on a tridiagonal matrix. This algorithm works on matrices
    with bandwidth 2p + 1 for p = 1.

    Args:
        epsilon: a constant
        n: integer in range 1 to 8
    Returns:
        A Tuple containing the x and u vectors
    """
    # Initialize variables that do not need calculations
    N = (2 ** n) - 1
    h = 2 ** (-n)
    a = q = -epsilon  # a and q are always equal to epsilon
    b = [(2 * epsilon + (h ** 2)) for _ in range(N)]
    # Note that we can initially multiply the f vector by h^2 since the A matrix contains a 1/h^2 term
    f = [((h ** 2) * (2 * i * h + 1)) for i in range(N)]

    # Forward Elimination
    w = [0 for _ in range(N)]
    w[0] = b[0]
    l = [0 for _ in range(N)]

    # Backward Substitution
    for k in range(1, N):
        l[k] = a / w[k - 1]
        w[k] = b[k] - l[k] * q

    y = [0 for _ in range(N)]
    y[0] = f[0]

    for k in range(1, N):
        y[k] = f[k] - l[k] * y[k - 1]

    # Solve for U (Au = f)
    u = [0 for _ in range(N)]
    u[N - 1] = y[N - 1] / w[N - 1]

    for k in reversed(range(N - 1)):
        u[k] = (y[k] - q * u[k + 1]) / w[k]

    x = [i * h for i in range(N)]

    # Return a tuple of the x vector along with the calculated u vector
    return x, u
