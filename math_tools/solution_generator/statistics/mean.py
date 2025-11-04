from statistics import mean as m
from math_tools.tools.latex import frac, new_line, get_mean_symbol
from .lib import StatisticsEquation


class Mean(StatisticsEquation):
	@property
	def result(self):
		return round(m(self.data), 2)

	@property
	def latex(self):
		if self.population not in ["full", "sample"]:
			raise Exception("Invalid population")

		points_mean = self.result
		points_stringified = " + ".join(list(map(str, self.data)))
		points_len = len(self.data)
		prefix = get_mean_symbol(self.population, self.label)
		self.output = f"{'\t' * self.tabs}{prefix}{frac(points_stringified, points_len)} = {frac(sum(self.data), points_len)} = {points_mean} {new_line()}"
		
		return super(StatisticsEquation, self).latex
