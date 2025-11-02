from .lib import StatisticsEquation
from .grouped_data_variance import GroupedDataVariance


class GroupedDataSD(StatisticsEquation):
	def __init__(self, data, label=None, population="full", tabs=1, environment=True):
		super().__init__(data, label, population, tabs, environment)
		self.gdv = GroupedDataVariance(
			self.data,
			self.label,
			self.population,
			self.tabs,
			False
		)

	@property
	def result(self):
		pass

	@property
	def latex(self):
		pass
