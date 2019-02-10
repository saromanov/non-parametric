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
        """ return mean from dataset
        """
        return np.mean(self._dataset)
    
    def __len__(self):
        """ returns length of array
        """
        return np.shape
    
    def std(self):
        """ return standard deviation of the dataset
        """
        return np.std(self._dataset)
    