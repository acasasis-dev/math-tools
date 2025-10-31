from math_tools.tools.latex import frac, text, new_line
from .lib import StatisticsEquation
from .mean import Mean
from .variance import Variance


class Correlation(StatisticsEquation):
	def __init__(self, data, label=("x", "y"), population="full", tabs=1, environment=True):
		super().__init__(data, label, population, tabs, environment)
		if len(self.data) != 2:
			raise Exception(f"length of data must exactly be 2")
		
		self.x, self.y = data
		if len(self.x) != len(self.y):
			raise Exception(f"length of x must be the same as y. {len(self.x)} != {len(self.y)}")
		
		if len(self.label) != 2:
			raise Exception(f"length of labels must exactly be 2")
		
		self.x_label, self.y_label = self.label
