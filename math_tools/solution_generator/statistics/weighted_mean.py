from .lib import StatisticsEquation
from math_tools.tools.latex import frac, get_mean_symbol, new_line


class WeightedMean(StatisticsEquation):
	def __init__(self, data=[], label=("x", "y"), population="full", tabs=1, environment=True):
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
		
		self.freq_total = sum(self.y)
		self.numerator = sum([num * self.y[i] for i, num in enumerate(self.x)])

	@property
	def result(self):
		return self.numerator / self.freq_total

	@property
	def latex(self):
		output = ""
		prefix = f"{"\t" * self.tabs}{get_mean_symbol(self.population)}"
		numerator = " + ".join([f"[({num})({self.y[i]})]" for i, num in enumerate(self.x)])
		denominator = " + ".join(list(map(str, self.y)))
		output += f"{prefix}{frac(numerator, denominator)} {new_line()}"
		numerator = " + ".join([f"{num * self.y[i]}" for i, num in enumerate(self.x)])
		output += f"{prefix}{frac(numerator, self.freq_total)} {new_line()}"
		output += f"{prefix}{frac(self.numerator, self.freq_total)} {new_line()}"

		if self.environment:
			output = (
				"\\begin{gather*}\n"
				f"{output}"
				"\\end{gather*}"
			)

		return output
