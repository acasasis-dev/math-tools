from .lib import StatisticsEquation
from .grouped_data_variance import GroupedDataVariance

from math import sqrt
from math_tools.tools.latex import new_line, sqrt as s


class GroupedDataSD(StatisticsEquation):
	def __init__(self, data, label=("x", "y"), population="full", tabs=1, environment=True):
		super().__init__(data, label, population, tabs, environment)
		self.gdsd = GroupedDataVariance(
			self.data,
			self.label,
			self.population,
			self.tabs,
			False
		)

	@property
	def result(self):
		return round(sqrt(self.gdsd.result), 2)

	@property
	def latex(self):
		output = self.gdsd.latex + f"{new_line() * 2}"
		output += f"{self.gdsd.prefix}{s(self.gdsd.result)} {new_line()}"
		output += f"{self.gdsd.prefix}{self.result} \n"

		if self.environment:
			output = (
				"\\begin{gather*}\n"
				f"{output}"
				"\\end{gather*}"
			)

		return output
