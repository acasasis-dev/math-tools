from .lib.covariance import covariance as cov
from .lib.mean import mean as m


def covariance(*args):
	return cov(*args)


def mean(*args):
	return m(*args)
