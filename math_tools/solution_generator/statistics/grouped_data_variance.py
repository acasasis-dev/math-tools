from .lib import StatisticsEquation


class GroupedDataVariance(StatisticsEquation):
	def __init__(self, data, label=None, population="full", tabs=1, environment=True):
		super().__init__(data, label, population, tabs, environment)

	@property
	def result(self):
		pass

	@property
	def latex(self):
		pass
	