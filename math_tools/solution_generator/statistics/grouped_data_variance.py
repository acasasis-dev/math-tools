from .lib import StatisticsEquation
from .grouped_data_mean import GroupedDataMean

from math_tools.tools.latex import get_sd_symbol


class GroupedDataVariance(StatisticsEquation):
	def __init__(self, data, label=("x", "y"), population="full", tabs=1, environment=True):
		super().__init__(data, label, population, tabs, environment)
		gdm = GroupedDataMean(
			self.data,
			self.label,
			self.population,
			self.tabs,
			False
		)
		self.numerator = round(sum([num * ((gdm.midpoints[i] - gdm.result)**2) for i, num in enumerate(gdm.y)]), 2)
		self.denominator = sum(gdm.y) - (1 if self.population == "sample" else 0)
		self.gdm_latex = gdm.latex

	@property
	def result(self):
		return round(self.numerator / self.denominator, 2)

	@property
	def latex(self):
		prefix = get_sd_symbol(self.population, self.label, variance=True)
		output = self.gdm_latex

		return output
	