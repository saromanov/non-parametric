from numpy.random import seed
from numpy.random import randn
import numpy as np


class Dataset:
    """this class contains dataset which is
    numpy array
    """
    def __init__(self, dataset):
        self._dataset = dataset
    
    def mean(self):
        return np.mean(self._dataset)
    
    def std(self):
        return np.std(self._dataset)
    