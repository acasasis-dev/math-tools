from math_tools.tools.latex import frac, text, new_line
from .lib import StatisticsEquation
from .mean import Mean
from .covariance import Covariance


class Correlation(StatisticsEquation):
	def __init__(self, data=[], label=("x", "y"), population="full", tabs=1, environment=True, covariance=None, x_sd=None, y_sd=None):
		super().__init__(data, label, population, tabs, environment)
	
	@property
	def result(self):
		pass

	@property
	def latex(self):
		pass
