from math_tools.tools.latex import frac, text, new_line
from .lib import StatisticsEquation
from .mean import Mean
from .covariance import Covariance


class Correlation(StatisticsEquation):
	def __init__(self, data=[], label=("x", "y"), population="full", tabs=1, environment=True, covariance=None, x_sd=None, y_sd=None):
		super().__init__(data, label, population, tabs, environment)
		if not covariance:
			if len(self.data) != 2:
				raise Exception(f"length of data must exactly be 2")
			
			self.x, self.y = data
			if len(self.x) != len(self.y):
				raise Exception(f"length of x must be the same as y. {len(self.x)} != {len(self.y)}")
			
			if len(self.label) != 2:
				raise Exception(f"length of labels must exactly be 2")
			
			self.x_label, self.y_label = self.label
			_covariance = Covariance(
				self.data,
				self.label,
				self.population,
				self.tabs,
				self.environment
			)
			self.covariance = _covariance.result
		else:
			self.covariance = covariance

		if not x_sd:
			pass
		else:
			self.x_sd = x_sd

		if not y_sd:
			pass
		else:
			self.y_sd = y_sd
	
	@property
	def result(self):
		return round(self.covariance / (self.x_sd * self.y_sd), 2)

	@property
	def latex(self):
		pass
