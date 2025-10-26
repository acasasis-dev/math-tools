from .lib.covariance import covariance as cov
from .lib.mean import mean as m
from .lib.variance import variance as v
from .lib.standard_deviation import standard_deviation as sd


def covariance(*args, **kwargs):
	return cov(*args, **kwargs)


def mean(*args, **kwargs):
	return m(*args, **kwargs)


def variance(*args, **kwargs):
	return v(*args, **kwargs)


def standard_deviation(*args, **kwargs):
	return sd(*args, **kwargs)
