from math_tools.common.equation import Equation


class StatisticsEquation(Equation):
	def __init__(self, data, label=None, population="full", tabs=1, environment=True):
		self.data = data
		self.label = label
		self.population = population
		self.tabs = tabs
		self.environment = environment
		