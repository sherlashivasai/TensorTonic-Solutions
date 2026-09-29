import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    arr = np.asarray(X, dtype = float)
    N = arr.shape[0]

    X_c = arr - (np.mean(arr, axis =0))

    return ((X_c.T@X_c)/(N-1))
    