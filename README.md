# non-parametric
Implementation of [non-parametric](https://en.wikipedia.org/wiki/Nonparametric_statistics) tests

### Install
```pip install nonparametric```

### Usage

Create a new dataset
```python
from numpy.random import randn, seed
seed(1)
data1 = randn(100)
```

Using `rank` method
```python
print(nonparametric.rank(ds))
```

Using Kolmogorov-Smirnov test
```python
print(nonparametric.kolmogorov_smirnov(ds))
```
