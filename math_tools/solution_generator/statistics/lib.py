from math_tools.common.equation import Equation


class StatisticsEquation(Equation):
	def __init__(self, data, label=None, population="full", tabs=1, environment=True):
		super().__init__(label, tabs, environment)
		self.data = data
		self.population = population
		