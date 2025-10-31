from .lib import StatisticsEquation
from .covariance import Covariance
from .standard_deviation import StandardDeviation


class Correlation(StatisticsEquation):
	def __init__(self, data=[], label=("x", "y"), population="full", tabs=1, environment=True, covariance=None, x_sd=None, y_sd=None):
		super().__init__(data, label, population, tabs, environment)
		if self.data and len(self.data) != 2:
			raise Exception(f"length of data must exactly be 2")
		elif self.data:
			self.x, self.y = data

		if not covariance:
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
			_x_sd = StandardDeviation(
				self.x,
				self.label,
				self.population,
				self.tabs,
				self.environment
			)
			self.x_sd = _x_sd.result
		else:
			self.x_sd = x_sd

		if not y_sd:
			_y_sd = StandardDeviation(
				self.y,
				self.label,
				self.population,
				self.tabs,
				self.environment
			)
			self.y_sd = _y_sd.result
		else:
			self.y_sd = y_sd
	
	@property
	def result(self):
		return round(self.covariance / (self.x_sd * self.y_sd), 2)

	@property
	def latex(self):
		pass
