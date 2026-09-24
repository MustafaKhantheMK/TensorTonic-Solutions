import numpy as np
import math

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    x_ = np.array(x)
    return 1 / (1 + np.exp(-x_))
    
    