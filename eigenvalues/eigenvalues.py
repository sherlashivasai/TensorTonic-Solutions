import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    eigvals = np.linalg.eigvals(matrix)
    
    # 2. Extract the real part (cleans up any +0.j complex float representations)
    real_eigvals = eigvals.real.astype(float)
    
    # 3. Return sorted in ascending order
    return np.sort(real_eigvals)