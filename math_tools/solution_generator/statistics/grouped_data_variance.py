from .lib import StatisticsEquation
from .grouped_data_mean import GroupedDataMean

from math_tools.tools.latex import get_sd_symbol, new_line, frac


class GroupedDataVariance(StatisticsEquation):
	def __init__(self, data, label=("x", "y"), population="full", tabs=1, environment=True):
		super().__init__(data, label, population, tabs, environment)
		self.gdm = GroupedDataMean(
			self.data,
			self.label,
			self.population,
			self.tabs,
			False
		)
		self.numerator = round(sum([num * ((self.gdm.midpoints[i] - self.gdm.result)**2) for i, num in enumerate(self.gdm.y)]), 2)
		self.denominator = sum(self.gdm.y) - (1 if self.population == "sample" else 0)

	@property
	def result(self):
		return round(self.numerator / self.denominator, 2)

	@property
	def latex(self):
		prefix = f"{"\t" * self.tabs}{get_sd_symbol(self.population, self.label, variance=True)}"
		output = self.gdm.latex + (new_line() * 2)
		numerator = " + ".join([f"[{num}({self.gdm.midpoints[i]} - {self.gdm.result})^2]" for i, num in enumerate(self.gdm.y)])
		denominator = " + ".join(list(map(str, self.gdm.y)))
		denominator = f"({denominator}) - 1" if self.population == "sample" else denominator
		output += f"{prefix}{frac(numerator, denominator)} {new_line()}"
		numerator = " + ".join([f"[{num}({round(self.gdm.midpoints[i] - self.gdm.result, 2)})^2]" for i, num in enumerate(self.gdm.y)])
		denominator = sum(self.gdm.y)
		denominator = f"{denominator} - 1" if self.population == "sample" else denominator
		output += f"{prefix}{frac(numerator, denominator)} {new_line()}"
		numerator = " + ".join([f"({num})({round((self.gdm.midpoints[i] - self.gdm.result) ** 2, 2)})" for i, num in enumerate(self.gdm.y)])
		output += f"{prefix}{frac(numerator, self.denominator)} {new_line()}"

		if self.environment:
			output = (
				"\\begin{gather*}\n"
				f"{output}"
				"\\end{gather*}"
			)

		return output
	