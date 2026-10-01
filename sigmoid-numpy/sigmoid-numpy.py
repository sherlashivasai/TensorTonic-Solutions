import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    # for scalar
    if isinstance(x,(int,  float)):
        if x>= 0:
            return 1/(1+ np.exp(-x))
        return np.exp(x)/(1+ np.exp(x))

    # for vectors/list

    arr = np.array(x,dtype = float)
    out = np.empty_like(arr)

    pos_mask = arr>= 0
    out[pos_mask] = 1/(1 + np.exp(-arr[pos_mask]))
    out[~pos_mask] = np.exp(arr[~pos_mask])/(1 + np.exp(arr[~pos_mask]))

    return out