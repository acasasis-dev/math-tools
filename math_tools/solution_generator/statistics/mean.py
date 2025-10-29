from statistics import mean as m
from math_tools.tools.latex import frac, new_line, mu, x_bar
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
		prefix = mu(self.label) if self.population == "full" else x_bar(self.label)
		output = f"{'\t' * self.tabs}{prefix} = {frac(points_stringified, points_len)} = {frac(sum(self.data), points_len)} = {points_mean} {new_line()}"
		if self.environment:
			output = (
				"\\begin{gather*} \n"
				f"{output}"
				"\\end{gather*}"
			)

		return output
