import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    res = []
    for i in x:
        if i >0:
            res.append(float(i))
        else:
            res.append(float(alpha *(math.exp(i)-1.0)))

    return res