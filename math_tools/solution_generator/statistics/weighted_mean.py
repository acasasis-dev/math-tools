from .lib import StatisticsEquation


class WeightedMean(StatisticsEquation):
	def __init__(self, data, label=None, population="full", tabs=1, environment=True):
		super().__init__(data, label, population, tabs, environment)

