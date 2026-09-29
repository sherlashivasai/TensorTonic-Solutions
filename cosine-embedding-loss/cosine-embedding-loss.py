import math
import numpy as np 

def cosine_embedding_loss(x1: list, x2: list, label: int, margin: float) -> float:
    """
    Returns the cosine embedding loss as a float.
    """
    # Write code here
    dot_p = np.dot(x1,x2)
    cos_p = dot_p/(np.dot(np.linalg.norm(x1),np.linalg.norm(x2)))
    loss = 0.0
    if label ==1:
        loss = 1 - cos_p

    else:
        loss = max(0,cos_p -margin)

    return float(loss)

    """ Without Numpy
    
    # 1. Compute dot product and squared magnitudes using zip and sum
    dot_product = sum(a * b for a, b in zip(x1, x2))
    norm_x1 = math.sqrt(sum(a * a for a in x1))
    norm_x2 = math.sqrt(sum(b * b for b in x2))

    # 2. Compute cosine similarity
    cos_sim = dot_product / (norm_x1 * norm_x2)

    # 3. Apply the loss formula based on the label
    if label == 1:
        return float(1.0 - cos_sim)
    else:
        return float(max(0.0, cos_sim - margin))

        """
    