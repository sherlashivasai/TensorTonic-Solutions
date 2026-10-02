import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Write code here
    arr = np.asarray(x, dtype = float)
    arr[arr<0] = alpha*arr[arr<0]
    return arr