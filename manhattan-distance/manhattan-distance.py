import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    # Write code here
    diff = np.asarray(x)- np.asarray(y)
    return float(np.linalg.norm(diff, ord = 1))