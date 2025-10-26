from .lib.covariance import covariance as cov
from .lib.mean import mean as m
from .lib.variance import variance as v


def covariance(*args):
	return cov(*args)


def mean(*args):
	return m(*args)


def variance(*args):
	return v(*args)
