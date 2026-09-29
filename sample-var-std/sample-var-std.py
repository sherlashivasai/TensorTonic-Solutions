import numpy as np
import math 
def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    mean = np.mean(x)

    val = 0
    for i in x:
        val += ((i-mean)**2)

    n = len(x)

    variance = val * (1/(n-1))

    sd = math.sqrt(variance)

    return { "variance": float(variance), "standard_deviation": float(sd) }