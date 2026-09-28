import numpy as np

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    diff = np.asarray(x, dtype='float') - np.asarray(y, dtype = 'float')
    return float(np.linalg.norm(diff))