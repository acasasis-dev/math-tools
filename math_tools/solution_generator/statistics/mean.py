from statistics import mean as m
from math_tools.tools.latex import frac, new_line, mu, x_bar
from math_tools.common.equation import Equation


class Mean(Equation):
	def __init__(self, data, label=None, population="full", tabs=1, environment=True):
		self.data = data
		self.label = label
		self.population = population
		self.tabs = tabs
		self.environment = environment

	@property
	def latex(self):
		if self.population not in ["full", "sample"]:
			raise Exception("Invalid population")

		points_mean = round(m(self.data), 2)
		self.result = points_mean
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
