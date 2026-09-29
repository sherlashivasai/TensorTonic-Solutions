import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a float.
    """
    # Write code here
    m = len(A)
    n = len(A[0])

    trace = 0.0
    for i in range(n):
        trace += A[i][i]

    return trace

    
                