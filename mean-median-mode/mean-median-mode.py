from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    frequencies = Counter(x)
    max_freq = max(frequencies.values())
    
    mode = min([float(key) for key, val in frequencies.items() if val == max_freq])
    
    return {
        "mean": float(np.mean(x)),
        "median": float(np.median(x)),
        "mode":float(mode)
    }