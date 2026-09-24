import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x_ = np.array(x)
    
    
    if x_.ndim > 0:
        for index,i in np.ndenumerate(x_):
            if x_[index] > 0:
                x_[index] = i
            if x_[index] <= 0:
                x_[index] = 0
    else:
        if x_ > 0:
            return x_
        return np.array(0)
    return x_