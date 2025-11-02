from .lib import StatisticsEquation
from math_tools.tools.latex import new_line, frac


class GroupedDataMean(StatisticsEquation):
	def __init__(self, data, label=("x", "y"), population="full", tabs=1, environment=True):
		super().__init__(data, label, population, tabs, environment)
		if self.data and len(self.data) != 2:
			raise Exception(f"length of data must exactly be 2")
		elif self.data:
			self.x, self.y = data
		else:
			self.x, self.y = [[], []]

		if len(self.label) != 2:
			raise Exception(f"length of labels must exactly be 2")
			 
		self.x_label, self.y_label = self.label
		self.label = f"{self.x_label}{self.y_label}" if len(self.x_label) + len(self.y_label) == 2 else f"[{self.x_label}, {self.y_label}]"
		self.denominator = sum(self.y)
		self.midpoints = [start + ((end - start) / 2) for start, end in self.x]
		self.numerator = round(sum([num * self.midpoints[i] for i, num in enumerate(self.y)]), 2)

	@property
	def result(self):
		return round(self.numerator / self.denominator, 2)

	@property
	def latex(self):
		ranges = [f"{self.x[i]}: {num}" for i, num in enumerate(self.y)]
		output = f"{"\t" * self.tabs}{", ".join(ranges)} {new_line() * 2}"
		numerator = " + ".join([f"[({num})({int(self.midpoints[i])})]" for i, num in enumerate(self.y)])
		denominator = " + ".join(list(map(str, self.y)))
		output += f"{"\t" * self.tabs}{frac(numerator, denominator)} {new_line()}"

		if self.environment:
			output = (
				"\\begin{gather*}\n"
				f"{output}"
				"\\end{gather*}"
			)

		return output
