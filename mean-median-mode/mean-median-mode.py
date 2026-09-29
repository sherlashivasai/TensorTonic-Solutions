from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    central_ten = {}
    central_ten['mean'] = float(np.mean(x))
    central_ten['median'] = float(np.median(x))

    #mode using counter
    counts = Counter(x)
    max_freq = max(counts.values())
    mode_val = float(min(val for val, freq in counts.items() if freq == max_freq))
    central_ten['mode'] = mode_val

    return central_ten