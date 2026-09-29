import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    return np.transpose(A)

    """
    n = len(A)
    m = len(A[0])

    # Swap coordinates (i, j) -> (j, i) manually
    transposed = [[A[i][j] for i in range(n)] for j in range(m)]

    return np.array(transposed
    """