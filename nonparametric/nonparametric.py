from numpy.random import seed, randn
import numpy as np
from scipy.stats import mannwhitneyu, rankdata, wilcoxon, kstest


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
    stat, p = mannwhitneyu(data1.dataset, data2.dataset)
    return True if p > alpha else False

def wilcoxon_sgned_rank(ds1, ds2, alpha=0.05):
    """ is a non-parametric statistical hypothesis test used to compare two 
    related samples, matched samples, or repeated measurements on a single 
    sample to assess whether their population mean ranks differ 
    (i.e. it is a paired difference test).
    """
    if not isinstance(ds1, Dataset) or not isinstance(ds2, Dataset):
        raise Exception("input data not is Dataset type")
    stat, p = wilcoxon(data1.dataset, data2.dataset)
    return True if p > alpha else False


def rank(ds):
    """rank of numerical dataset
    """
    if not isinstance(ds, Dataset):
        raise Exception("input data is not Dataset type")
    return rankdata(ds.dataset)

def kolmogorov_smirnov(ds, cdf='norm', n=20, alpha=0.05):
    """is a nonparametric test of the equality of continuous, 
    one-dimensional probability distributions that can be used 
    to compare a sample with a reference probability distribution
    """
    if not isinstance(ds, Dataset):
        raise Exception("input data is not Dataset type")
    stat, p = kstest(ds.dataset, cdf, N=n)
    return True if p > alpha else False

    
    