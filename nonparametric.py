from numpy.random import seed, randn
import numpy as np
from scipy.stats import mannwhitneyu, rankdata


class Dataset:
    """this class contains dataset which is
    numpy array
    """
    def __init__(self, dataset):
        self.dataset = dataset
    
    def mean(self):
        """ return mean from dataset
        """
        return np.mean(self.dataset)
    
    def __len__(self):
        """ returns length of array
        """
        return np.shape
    
    def std(self):
        """ return standard deviation of the dataset
        """
        return np.std(self.dataset)

def mann_whitney_u(ds1, ds2, alpha=0.05):
    """ this method return True if this is same
    distribution(fail to reject H0) and False if this different distributions
    """
    if not isinstance(ds1, Dataset) or not isinstance(ds2, Dataset):
        raise Exception("input data not is Dataset type")
    stat, p = mannwhitneyu(data1, data2)
    return True if p > alpha else False


def rank(ds):
    """rank of numerical dataset
    """
    return rankdata(ds)

    
    