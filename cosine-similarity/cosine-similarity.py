import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """Return the cosine similarity of a and b."""
    # Write code here
    if not np.any(a):
        return float(0)
    if not np.any(b):
        return float(0)
    return float(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b)))