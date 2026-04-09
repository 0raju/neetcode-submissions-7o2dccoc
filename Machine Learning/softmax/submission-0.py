import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        softmax_z = np.exp(z-np.max(z))
        
        return np.round(softmax_z/softmax_z.sum(axis=0), 4)

